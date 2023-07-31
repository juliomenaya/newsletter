from django.core.management.base import BaseCommand
from faker import Faker
from newsletters.models import Newsletter, Recipient, Email


class Command(BaseCommand):
    help = 'Populate initial data using Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()

        newsletter = Newsletter.objects.create(name='Promotions')

        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            r = Recipient.objects.create(first_name=first_name, last_name=last_name, email=email)
            r.newsletters.add(newsletter)

        all_recipients = Recipient.objects.all()

        for _ in range(50):
            subject = fake.sentence(nb_words=4)
            body = fake.text()
            email = Email.objects.create(subject=subject, body=body, newsletter=newsletter)
            email.recipients.add(*all_recipients)
