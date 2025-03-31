from django.urls import path
from .views import create_chatbot,get_chatbot_by_id

urlpatterns = [
    path('chatbots/',create_chatbot, name= 'create_chatbot'),
    path('chatbots/<int:chatbot_id>/', get_chatbot_by_id, name='get_chatbot_by_id'),
]