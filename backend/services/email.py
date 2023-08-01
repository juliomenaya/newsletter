from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class EmailSender:
    def __init__(self, subject, template_name, context, from_email, recipient_list, attachment_path=None):
        self.subject = subject
        self.template_name = template_name
        self.context = context
        self.from_email = from_email
        self.recipient_list = recipient_list
        self.attachment_path = attachment_path

    def send_email(self):
        try:
            html_message = render_to_string(self.template_name, self.context)
            plain_message = strip_tags(html_message)
            email = EmailMultiAlternatives(
                self.subject,
                plain_message,
                self.from_email,
                self.recipient_list,
            )
            email.attach_alternative(html_message, 'text/html')

            if self.attachment_path:
                email.attach(self.attachment_path.split('/')[-1], open(self.attachment_path, 'rb').read())

            email.send()
            return True, 'Email sent successfully.'
        except Exception as e:
            raise e
            return False, f'Email failed to send. Error: {e}'
