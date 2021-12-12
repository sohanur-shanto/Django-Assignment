from django.db.models.query import QuerySet
from django.shortcuts import render
from . serializers import *
from rest_framework.generics import ListAPIView
from . models import *
from django.db.models import Q
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__username', 'gender', 'city', 'zip', 'phone', ]
    
    # filter_backends = [SearchFilter]
    # search_fields = ['^user__username', '^address',]
    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Profile.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(address__icontains=query)|
    #             Q(user__username__icontains=query)
    #         ).distinct()
    #     return queryset_list
