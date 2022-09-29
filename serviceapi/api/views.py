from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import added_to_db
from .googleapi import GoogleApi

# Create your views here.


def index(request):
    gsi = GoogleApi()
    list_to_db = gsi.get_rows(ranges='List1')
    return print(added_to_db(list_data=list_to_db))


class Home(ListView):
    model = Ticket
    context_object_name = 'Ticket'
    template_name = 'api/ticket_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Ticket.objects.all()

