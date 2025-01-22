from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data_preprocessing import get_chatbot_response

class ChatbotAPIView(APIView):
    def post(self, request):
        # Extract the user query from the request data
        user_query = request.data.get('query', None)
        
        if user_query is None:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the chatbot's response
        response = get_chatbot_response(user_query)
        
        # Return the response as JSON
        return Response({"response": response}, status=status.HTTP_200_OK)
