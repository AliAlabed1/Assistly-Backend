from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import chatbotSerializer,ChatbotCharactersticsSerializer
from .models import Chatbot,ChatbotCharacteristic


@api_view(['POST'])
def create_chatbot(request):
    serializer = chatbotSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_chatbot_by_id(request,chatbot_id):
    try:
        chatbot = Chatbot.objects.get(id = chatbot_id)
    except Chatbot.DoesNotExist:
        return Response({"error": "Chatbot not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = chatbotSerializer(chatbot)
    return Response(serializer.data)
