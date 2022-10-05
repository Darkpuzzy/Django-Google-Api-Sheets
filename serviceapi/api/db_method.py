from .models import Ticket
from .googleapi import GoogleApi
from time import sleep
# ['id', 'order', 'price_dlr', 'deliv_data', 'price_in_ru'] Table input


def added_to_db(list_data: list):
    try:
        for elements in list_data:
            model = Ticket(*elements)
            model.save()
        return print('Success')
    except:
        return 'ERROR\nPlease ask administration'

# List comparison ( db == Google Sheet )


def _list_orders(list_data_get: list):
    list_output = []
    orders = map(list, list_data_get)
    for item in orders:
        x = item[1]
        list_output.append(x)
    return list_output

# Check data from Google Api Sheets


def _updated_data(list_data: list):
    orders = _list_orders(list_data_get=list_data)
    model = Ticket.objects.all()
    for items in model:
        if items.order not in orders:
            Ticket.objects.filter(order=items.order).delete()
        else:
            print(orders)
            # orders.clear()
            return print('Not updated')
# Activate up functions


def main():
    gsi = GoogleApi()
    while True:
        list_to_db = gsi.get_rows(ranges='List1')
        sleep(4)
        added_to_db(list_data=list_to_db)
        _updated_data(list_data=list_to_db)



