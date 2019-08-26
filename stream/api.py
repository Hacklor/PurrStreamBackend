from django.http import JsonResponse
from rest_framework import viewsets, mixins
from rest_framework.renderers import JSONRenderer

from stream.models import Purr
from stream.serializers import PurrSerializer

class PurrViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Purr.objects.all()
    serializer_class = PurrSerializer
