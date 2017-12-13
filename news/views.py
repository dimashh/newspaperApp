# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from news.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    # API end to allow users to be viewed or edited
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
