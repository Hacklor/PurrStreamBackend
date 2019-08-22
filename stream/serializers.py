from rest_framework import serializers

from stream.models import Purr

class PurrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purr
        fields = ['id', 'author', 'content']
