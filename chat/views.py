from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import chatbotSerializer,ChatbotCharactersticsSerializer,ChatSessionSerializer
from .models import Chatbot,ChatbotCharacteristic,ChatSession
from django.http import JsonResponse
from django.utils import timezone

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

@api_view(["GET"])
def get_user_chatbots(request,user_id):
    try:
        chatbots = Chatbot.objects.filter(clerk_user_id = user_id)
        serializer = chatbotSerializer(chatbots,many=True)
    except Exception as e:
        return Response({"error":"Unexpected error"})
    return Response(serializer.data)
        

@api_view(["DELETE"])
def delete_chatbot_characteristic(request,characteristic_id):
    try:
        characteristic = ChatbotCharacteristic.objects.get(id=characteristic_id)
        characteristic.delete()
        return Response({"message":"Characteristic deleted!"},status=status.HTTP_204_NO_CONTENT)
    except ChatbotCharacteristic.DoesNotExist:
        return Response({"message":"Characteristic not found!"},status=status.HTTP_404_NOT_FOUND)
    
@api_view(["DELETE"])
def delete_chatbot(request,chatbot_id):
    try:
        chatbot = Chatbot.objects.get(id=chatbot_id)
        chatbot.delete()
        return Response({"message":"Chatbot deleted!"},status=status.HTTP_204_NO_CONTENT)
    except Chatbot.DoesNotExist:
        return Response({"message":"Chatbot not found!"},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def create_characteristic(request):
    print(request.data)
    serializer = ChatbotCharactersticsSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_chatbot_name(request):
    try:
        chatbot = Chatbot.objects.get(id = request.data['id'])
        chatbot.name = request.data['new_name']
        chatbot.created_at = timezone.now()
        chatbot.save()
        return JsonResponse({'message':"Chatbot name updated successfully!"})
    except Chatbot.DoesNotExist:
        return JsonResponse({"message":"Chatbot not exsist"},)

@api_view(["GET"])
def get_session_by_id(request,session_id):
    try:
        session = ChatSession.objects.get(id = session_id)
    except ChatSession.DoesNotExist:
        return Response({"message":"Session does not exist"},status=status.HTTP_404_NOT_FOUND)
    serializer = ChatSessionSerializer(session)
    return Response(serializer.data)