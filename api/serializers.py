
from rest_framework import serializers
from .models import spam_ham

class spamserializers(serializers.ModelSerializer):
    class Meta:
        model = spam_ham
        fields = ['text','result']