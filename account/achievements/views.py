import requests
from rest_framework import viewsets
from rest_framework.response import Response

from achievements.serializers import ImageSerializer
from achievements.models import *


class ImagesViewset(viewsets.ModelViewSet):
    queryset = AccountPhoto.objects.all()
    serializer_class = ImageSerializer
