from django.core.management.base import BaseCommand
from newsletters.models import Newsletter, Recipient


class Command(BaseCommand):
    help = 'Populate initial data using Faker'

    def handle(self, *args, **kwargs):

        promo_newsletter, _ = Newsletter.objects.get_or_create(name='Promotions', email_template='promotion.html')
        monthly_newsletter, _ = Newsletter.objects.get_or_create(name='Monthly news', email_template='monthly_news.html')

        email = 'julio@yopmail.com'

        for i in range(1, 5):
            first_name = f'Julioncho_{i}'
            last_name = f'Mendez_{i}'
            email = f'julio_{i}@yopmail.com'
            r,_ = Recipient.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)
            r.newsletters.add(promo_newsletter)
            r.newsletters.add(monthly_newsletter)
