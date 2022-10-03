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
from .serializers import OrderSerializer
from .db_method import added_to_db, _updated_data
from .googleapi import GoogleApi


""" Для обработки нужно будет обновлять страницу,фикс постараться поискать"""


@api_view(['GET'])
def index(request, pk):
    status_code = status.HTTP_200_OK
    gsi = GoogleApi()
    list_to_db = gsi.get_rows(ranges='List1')
    model = Ticket.objects.get(pk=pk)

    response = {'order': model.order, 'price_dlr': model.price_dlr}
    print(_updated_data(list_data=list_to_db))
    print(added_to_db(list_data=list_to_db))
    return Response(response, status=status_code)


class OrderCreateList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = OrderSerializer


class Home(ListView):
    model = Ticket
    context_object_name = 'Ticket'
    template_name = 'api/ticket_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Ticket.objects.all()

