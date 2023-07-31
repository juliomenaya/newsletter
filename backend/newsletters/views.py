from django.conf import settings
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
        attachment = request.FILES.get('attachment')
        subject = 'Subject Test'
        template_name = 'promotion.html'
        context = {
            'username': 'John',
            'unsubscribe_link': f'{settings.APP_HOST}{reverse("newsletter-unsubscribe")}?recipient_id=1&newsletter_id=1',
            'newsletter_name': 'Awesome Newsletter',
        }
        from_email = 'sender@example.com'
        recipient_list = ['recipient1@example.com']

        email_sender = EmailSender(subject, template_name, context, from_email, recipient_list)
        sent, message = email_sender.send_email()

        if sent:
            return Response({'message': message, 'status': 200})
        else:
            return Response({'message': message, 'status': 400})

    @action(detail=False, methods=['get'])
    def unsubscribe(self, request):
        recipient = Recipient.objects.get(id=request.query_params['recipient_id'])
        Newsletter.objects.get(id=request.query_params['newsletter_id']).recipients.remove(recipient)
        return Response()
