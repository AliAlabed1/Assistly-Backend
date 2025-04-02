from rest_framework import serializers
from .models import Chatbot, ChatbotCharacteristic,ChatSession

class ChatbotCharactersticsSerializer(serializers.ModelSerializer):
    chatbot_id = serializers.PrimaryKeyRelatedField(
        queryset=Chatbot.objects.all(),
        source='chatbot'  
    )

    class Meta:
        model = ChatbotCharacteristic
        fields = ['id', 'chatbot_id', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']


class ChatSessionSerializer(serializers.ModelSerializer):
    chatbot_id = serializers.PrimaryKeyRelatedField(
        queryset=Chatbot.objects.all(),
        source='chatbot'  
    )
    class Meta:
        model = ChatSession
        fields = ['id','created_at','chatbot_id','guest_id']
        read_only_fields = ['id', 'created_at']

class chatbotSerializer(serializers.ModelSerializer):
    characteristics = ChatbotCharactersticsSerializer(many=True, read_only=True)
    chat_sessions = ChatSessionSerializer(many = True,read_only=True)
    class Meta:
        model = Chatbot
        fields = ['id','clerk_user_id','name','created_at','characteristics','chat_sessions']
        read_only_fields = ['id','created_at']
