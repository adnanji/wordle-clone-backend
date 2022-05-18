from rest_framework import serializers
from .models import WordleModel

class WordleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordleModel
        fields = ["pk", "wordle"]