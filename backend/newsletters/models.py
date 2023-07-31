from django.db import models
from core.base_model import BaseModel


class Recipient(BaseModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.email


class Newsletter(BaseModel):
    name = models.CharField(max_length=124, unique=True)
    subscribers = models.ManyToManyField(Recipient, related_name='newsletters')


    def __str__(self):
        return f'{self.name} Newsletter'


class Email(BaseModel):
    subject = models.CharField(max_length=124)
    body = models.TextField()
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='emails')
    recipients = models.ManyToManyField(Recipient, related_name='emails')

    def __str__(self):
        return self.subject
