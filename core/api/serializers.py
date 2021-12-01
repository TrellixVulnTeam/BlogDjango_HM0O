from rest_framework import serializers
from core import models


class PostSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Post
        fields = '__all__'
