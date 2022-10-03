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


def _list_orders(list_data_get: list):
    list_output = []
    orders = map(list, list_data_get)
    for item in orders:
        x = item[1]
        list_output.append(x)
    return list_output


def _updated_data(list_data: list):
    orders = _list_orders(list_data_get=list_data)
    appent = []
    model = Ticket.objects.all()
    for items in model:
        if items.order not in orders:
            appent.append(items.order)
            delet = Ticket.objects.filter(order=items.order).delete()
            delet.save()
    return appent
