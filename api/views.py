from django.shortcuts import render
from trombi import models
from api import serializers

class MessageViewSet(ReadOnlyViewSet):
    queryset= models.Message.objects.all()
    serializer_class = serializers
