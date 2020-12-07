from django.urls import path
from . import views


urlpatterns = [
    path('api/books/list/',views.BooksListApiView.as_view()),
    path('api/books/add/',views.BooksCreateApiView.as_view()),
    path('api/books/detail/<pk>/',views.BooksRetrieveAPIView.as_view()),
    path('api/books/delete/<pk>/',views.BooksDeleteAPIView.as_view()),
    path('api/books/update/<pk>/',views.BooksUpdateAPIView.as_view()),
    path('api/books/modify/<pk>/',views.BooksModifyAPIView.as_view())
]