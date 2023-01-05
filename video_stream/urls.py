from django.urls import path
from .views import VideoStreamListCreateAPIView, VideoStreamDetailDeleteAPIView, VideoStreamUpdateAPIView

urlpatterns = [
    path('', VideoStreamListCreateAPIView.as_view()),
    path('<int:pk>/update/', VideoStreamUpdateAPIView.as_view()),
    path('<int:pk>/', VideoStreamDetailDeleteAPIView.as_view()),
]