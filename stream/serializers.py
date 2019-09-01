from rest_framework import serializers

from stream.models import Purr

class PurrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purr
        fields = ['id', 'user_id', 'content', 'created_at']
        read_only_fields = ['created_at']
