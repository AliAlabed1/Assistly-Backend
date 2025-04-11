from rest_framework import serializers
from .models import Chatbot, ChatbotCharacteristic,ChatSession,Guest,Message

class MessagesSerialiser(serializers.ModelSerializer):
    chat_session_id = serializers.PrimaryKeyRelatedField(
        queryset = ChatSession.objects.all(),
        source = 'chat_session'
    )
    class Meta:
        model = Message
        fields = ['id','content','sender','created_at','chat_session_id']
        read_only_feilds = ['id','created_at']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id','email','name','created_at']
        read_only_fields = ['id','created_at']

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
    guest_id = serializers.PrimaryKeyRelatedField(
        queryset=Guest.objects.all(),
        source='guest'
    )
    chatbot_name = serializers.CharField(source='chatbot.name', read_only=True)
    guest = GuestSerializer(read_only = True)
    messages = MessagesSerialiser(read_only=True,many=True)
    class Meta:
        model = ChatSession
        fields = ['id','created_at','chatbot_id','guest_id','guest','messages','chatbot_name']
        read_only_fields = ['id', 'created_at']

class chatbotSerializer(serializers.ModelSerializer):
    characteristics = ChatbotCharactersticsSerializer(many=True, read_only=True)
    chat_sessions = ChatSessionSerializer(many = True,read_only=True)
    class Meta:
        model = Chatbot
        fields = ['id','clerk_user_id','name','created_at','characteristics','chat_sessions']
        read_only_fields = ['id','created_at']


