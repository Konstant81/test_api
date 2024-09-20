from rest_framework import serializers
from .models import Client, Send, Message


class ClientSerializer(serializers.ModelSerializer):
    # code = serializers.CharField(read_only = True)
    code = serializers.SerializerMethodField()
    class Meta:
        model= Client
        fields = '__all__'

    def get_code(self, obj):
        return obj.phone_number[1:4]
    def create(self, validated_data):
        validated_data['code'] = validated_data['phone_number'][1:4]
        return super().create(validated_data)
    def update(self, instance, validated_data):
        validated_data['code'] = validated_data['phone_number'][1:4]
        return super().update(instance, validated_data)

class SendSerializer(serializers.ModelSerializer):
    class Meta:
        model= Send
        fields = '__all__'

    def validate_code(self, code: str) -> str:
        if len(code) > 3 or len(code) < 1 or not code.isdigit():
            raise serializers.ValidationError('Код оператора должен иметь числовое значение и находиться в диапазоне 001...999')
        return code

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Message
        fields = '__all__'
