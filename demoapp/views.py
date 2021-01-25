from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def index(request):
    """
        Index for the app
    """
    return Response({'data': 'Hello World'}, status=status.HTTP_200_OK)
