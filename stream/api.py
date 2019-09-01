from django.http import JsonResponse
from rest_framework import viewsets, mixins
from rest_framework.exceptions import NotAuthenticated
from rest_framework.renderers import JSONRenderer

from stream.models import Purr
from stream.serializers import PurrSerializer

class PurrViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Purr.objects.all().order_by('-created_at')
    serializer_class = PurrSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated()
        serializer.save(user=user)
