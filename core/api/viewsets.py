from rest_framework import serializers, viewsets
from core.api.serializers import serializers
from core import models
from core.api import serializers


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializers
    queryset = models.Post.objects.all()