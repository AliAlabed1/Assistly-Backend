from django.urls import path
from .views import create_chatbot,get_chatbot_by_id,delete_chatbot_characteristic,delete_chatbot,get_user_chatbots,create_characteristic,update_chatbot_name

urlpatterns = [
    path('chatbots/',create_chatbot, name= 'create_chatbot'),
    path('chatbots/<int:chatbot_id>/', get_chatbot_by_id, name='get_chatbot_by_id'),
    path('characteristic_del/<int:characteristic_id>/',delete_chatbot_characteristic,name = 'delete_charbot_characteristic'),
    path('chatbot_del/<int:chatbot_id>/',delete_chatbot,name = 'delete_chatbot'),
    path('user_chatbots/<str:user_id>/',get_user_chatbots,name = 'get_user_chatbots'),
    path('characteristic/create/',create_characteristic,name = 'create_characteristic'),
    path('change_chatbot_name/',update_chatbot_name,name='update_chatbot_name')
]