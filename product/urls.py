from django.urls import path

from . import views

urlpatterns = [
    path('comment/', views.CommentCreateView.as_view()),
    path('comment/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
]