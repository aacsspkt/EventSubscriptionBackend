from rest_framework import generics, permissions
from rest_framework import filters
from rest_framework_simplejwt import authentication

from .serializers import VideoStreamSerializer
from .models import VideoStream
from user.permissions import IsAdminUserOrReadOnly

class VideoStreamListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = VideoStreamSerializer
    queryset = VideoStream.objects.all()
    permission_classes = [IsAdminUserOrReadOnly, permissions.IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class VideoStreamDetailDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = VideoStreamSerializer
    queryset = VideoStream.objects.all()
    permission_classes = [IsAdminUserOrReadOnly, permissions.IsAuthenticated, ]

class VideoStreamUpdateAPIView(generics.UpdateAPIView):
    serializer_class = VideoStreamSerializer
    queryset = VideoStream.objects.all()
    permission_classes = [permissions.IsAdminUser,]
