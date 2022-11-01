from rest_framework import status
from rest_framework.response import Response
import random
import time


def index(request):
    return Response({"status": "error", "data": "Missing integer quantity"}, status=status.HTTP_400_BAD_REQUEST)


def choice(request, quantity):
    if request.method != "GET":
        return Response({"status": "error", "data": "Improper request method"}, status=status.HTTP_400_BAD_REQUEST)

    random.seed(int(time.time()))
    image_choice = random.randint(1, quantity)
    return Response({"status": "success", "data": image_choice}, status=status.HTTP_200_OK)
