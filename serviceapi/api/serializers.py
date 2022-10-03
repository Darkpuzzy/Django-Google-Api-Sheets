from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ticket


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'order', 'price_dlr', 'price_in_ru', 'deliv_data')