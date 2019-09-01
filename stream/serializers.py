from rest_framework import serializers
from stream.models import User, Purr

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )

class PurrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purr
        fields = ['id', 'user', 'content', 'created_at']
        read_only_fields = ['created_at']

    user = NestedUserSerializer(read_only=True)
