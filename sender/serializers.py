from rest_framework import serializers
from .models import Client, Send, Message

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields = '__all__'

class SendSerializer(serializers.ModelSerializer):
    class Meta:
        model= Send
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Message
        fields = '__all__'