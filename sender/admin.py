from django.contrib import admin
from .models import Client, Send, Message
# Register your models here.

admin.site.register(Client)
admin.site.register(Send)
admin.site.register(Message)
