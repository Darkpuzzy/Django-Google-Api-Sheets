from django.contrib import admin
from .models import Ticket
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'price_dlr', 'deliv_data', 'price_in_ru', 'delivered']
    list_display_links = ['id', 'order']
    search_fields = ['order', 'deliv_data']
    list_filter = ('order', 'price_dlr', 'price_in_ru')


admin.site.register(Ticket, TicketAdmin)