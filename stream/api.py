from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from stream.models import Purr
from stream.serializers import PurrSerializer

@api_view(['GET'])
@parser_classes([JSONParser])
def purr_list(request):
    purrs = Purr.objects.all()
    serializer = PurrSerializer(purrs, many=True)
    return Response(serializer.data)
