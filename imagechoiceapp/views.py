
from rest_framework import status
from rest_framework.response import Response
import random
import time
from rest_framework.views import APIView


class IndexView(APIView):
    def get(self, request):
        responsejson = {"status": "error", "data": "Missing integer quantity"}
        return Response(responsejson)


class ChoiceView(APIView):
    def post(self, request):
        return Response({"status": "error", "data": "Improper request method"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, quantity):
        random.seed(int(time.time()))
        image_choice = random.randint(1, quantity)
        return Response({"status": "success", "data": image_choice}, status=status.HTTP_200_OK)
