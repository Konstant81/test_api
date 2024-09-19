from rest_framework import viewsets
from .serializers import ClientSerializer, SendSerializer, MessageSerializer
from .models import Client, Send, Message



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class SendViewSet(viewsets.ModelViewSet):
    queryset = Send.objects.all()
    serializer_class = SendSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
