from django.urls import path
from .views import ThingList, ThingDetail

urlpatterns = [
    path('', ThingList.as_view(), name='things_list'),
    path('/<int:pk>/', ThingDetail.as_view(), name='thing_detail'),
    # path('post/', PostsList.as_view(), name='posts_list'),
    # path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]