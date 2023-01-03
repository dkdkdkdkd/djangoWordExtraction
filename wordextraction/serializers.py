from rest_framework import serializers
from .models import WordDb

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordDb
        fields = '__all__'