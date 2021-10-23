from rest_framework import serializers

from .models import Note


class NoteSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'message', 'public', ]
