from django.core.exceptions import ValidationError
from django.db import models
from django.template.loader import get_template
from core.base_model import BaseModel


def validate_email_template(value):
    try:
        get_template(value)
    except Exception as e:
        raise ValidationError(f'Your template must be created before adding a Newsletter instance: {e}')


class Recipient(BaseModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.email


class NewsletterManager(models.Manager):
    def create(self, **kwargs):
        email_template = kwargs.get('email_template')
        if email_template:
            validate_email_template(email_template)
        return super().create(**kwargs)


class Newsletter(BaseModel):
    name = models.CharField(max_length=124, unique=True)
    subscribers = models.ManyToManyField(Recipient, related_name='newsletters')
    email_template = models.TextField(validators=[validate_email_template])

    objects = NewsletterManager()

    def __str__(self):
        return f'{self.name} Newsletter'


class Email(BaseModel):
    subject = models.CharField(max_length=124)
    body = models.TextField()
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='emails')
    recipients = models.ManyToManyField(Recipient, related_name='emails')

    def __str__(self):
        return self.subject
