from rest_framework import serializers
from .models import Chatbot, ChatbotCharacteristic

class ChatbotCharactersticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotCharacteristic
        fields = ['id','chatbot_id','content','created_at']

class chatbotSerializer(serializers.ModelSerializer):
    characteristics = ChatbotCharactersticsSerializer(many=True, read_only=True)

    class Meta:
        model = Chatbot
        fields = ['id','clerk_user_id','name','created_at','characteristics']
        read_only_fields = ['id','created_at']
