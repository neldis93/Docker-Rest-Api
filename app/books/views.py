from django.shortcuts import render
from .serializers import BooksSerializer
from .models import Books
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

class BooksListApiView(ListAPIView):
    serializer_class = BooksSerializer
    
    def get_queryset(self):
        return Books.objects.all()

class BooksCreateApiView(CreateAPIView):
     serializer_class = BooksSerializer

class BooksRetrieveAPIView(RetrieveAPIView):
    serializer_class = BooksSerializer
    queryset=Books.objects.all()

class BooksDeleteAPIView(DestroyAPIView):
    serializer_class = BooksSerializer
    queryset=Books.objects.all()

class BooksUpdateAPIView(UpdateAPIView):
    serializer_class = BooksSerializer
    queryset=Books.objects.all()

class BooksModifyAPIView(RetrieveUpdateAPIView):
    serializer_class = BooksSerializer
    queryset=Books.objects.all()
