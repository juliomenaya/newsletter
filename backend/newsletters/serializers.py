from rest_framework.serializers import ModelSerializer

from newsletters.models import Newsletter


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'
