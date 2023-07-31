from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from newsletters.models import Newsletter, Recipient
from newsletters.serializers import NewsletterSerializer
from services.email import EmailSender


class NewslettersModelViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    @action(detail=False, methods=['post'])
    def send(self, request):
        attachment = request.data.get('attachment')
        recipients = request.data.get('recipients')
        newsletter_id = request.data.get('newsletter_id')
        send_to_subscribers = request.data.get('send_to_subscribers')

        newsletter = Newsletter.objects.get(id=newsletter_id)

        subject = 'Subject Test'
        template_name = 'promotion.html'
        from_email = 'sender@example.com'

        unsubscribe_base_link = f'{settings.APP_HOST}{reverse("newsletter-unsubscribe")}'
        for recipient_email in recipients.split(','):
            recipient = Recipient.objects.filter(email=recipient_email.strip()).first()
            if recipient:
                context = {
                    'username': recipient,
                    'unsubscribe_link': f'{unsubscribe_base_link}?recipient_id={recipient.id}&newsletter_id={newsletter.id}',
                    'newsletter_name': newsletter.name,
                }
                email_sender = EmailSender(subject, template_name, context, from_email, [recipient.email])
                email_sender.send_email()

        if send_to_subscribers:
            for recipient in newsletter.subscribers.all():
                context = {
                    'username': recipient,
                    'unsubscribe_link': f'{unsubscribe_base_link}?recipient_id={recipient.id}&newsletter_id={newsletter.id}',
                    'newsletter_name': newsletter.name,
                }
                email_sender = EmailSender(subject, template_name, context, from_email, [recipient.email])
                email_sender.send_email()

        return Response({'message': 'Emails sent', 'status': 200})

    @action(detail=False, methods=['get'])
    def unsubscribe(self, request):
        try:
            recipient = Recipient.objects.get(id=request.query_params['recipient_id'])
            newsletter = Newsletter.objects.get(id=request.query_params['newsletter_id'])
            newsletter.subscribers.remove(recipient)
            context = {
                'recipient_name': f'{recipient.first_name} {recipient.last_name}',
                'newsletter_name': newsletter.name,
            }
            html_content = render(request, 'unsubscribe.html', context).content

            return HttpResponse(html_content, content_type='text/html')
        except (KeyError, ValueError, Recipient.DoesNotExist, Newsletter.DoesNotExist):
            return Response(status=400)
