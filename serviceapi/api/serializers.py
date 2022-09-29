from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ticket

# ['id', 'order', 'price_dlr', 'deliv_data', 'price_in_ru'] Table input


def added_to_db(list_data: list):
    try:
        for elements in list_data:
            model = Ticket(*elements)
            model.save()
        return print('Success')
    except:
        return 'ERROR\nPlease ask administration'

