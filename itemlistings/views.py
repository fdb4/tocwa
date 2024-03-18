from django.shortcuts import render
from rest_framework import generics, permissions
from .models import main
from .serializers import carribeanSerializer
# Create your views here.
class carribeanCreateView(generics.CreateAPIView):
    queryset = main.objects.all()
    serializer_class = carribeanSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class carribeanListView(generics.ListAPIView):
    queryset = main.objects.all()
    serializer_class = carribeanSerializer
    http_method_names = ['get']