# from django.shortcuts import render
# from rest_framework import generics
# from .models import Thing, Post 
# from .serializers import ThingSerializer, PostSerializer
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .permissions import IsOwnerOrReadOnly

# # Create your views here.

# # ListAPIView ListCreateAPIView
# class ThingsList(generics.ListCreateAPIView):
#     queryset = Thing.objects.all()
#     serializer_class = ThingSerializer
#     permission_classes = [IsAuthenticated]

# # RetrieveAPIView RetrieveUpdateAPIView RetrieveUpdateDestroyAPIView
# class ThingDetail(generics.RetrieveUpdateAPIView):
#     queryset = Thing.objects.all()
#     serializer_class = ThingSerializer
#     permission_classes = [IsOwnerOrReadOnly]

# # ListAPIView
# class PostsList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [AllowAny]

# # RetrieveAPIView RetrieveUpdateAPIView
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [AllowAny]

#---------------------------------
from rest_framework import generics
from .models import Thing
from .permissions import IsOwnerOrReadOnly
from .serializers import ThingSerializer


class ThingList(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer