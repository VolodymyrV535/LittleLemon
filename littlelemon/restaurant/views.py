from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import permissions
from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuItem, Booking
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer   
    permission_classes = [permissions.IsAuthenticated]
    

