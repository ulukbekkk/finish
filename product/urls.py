from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategotyListAPIView.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
    path('comment/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),

]