from django.db import models

class Chatbot(models.Model):
    clerk_user_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ChatbotCharacteristic(models.Model):
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name='characteristics')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Guest(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Anonymous Guest"

class ChatSession(models.Model):
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE,related_name='chat_sessions')
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True,related_name='guests')
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    sender = models.CharField(max_length=50)  # 'user' or 'ai'
    created_at = models.DateTimeField(auto_now_add=True)