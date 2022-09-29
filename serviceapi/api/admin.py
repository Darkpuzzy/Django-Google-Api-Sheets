from django.contrib import admin
from .models import Ticket
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price_dlr', 'deliv_data', 'price_in_ru', 'delivered']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'deliv_data']
    list_filter = ('title', 'price_dlr', 'price_in_ru')


admin.site.register(Ticket, TicketAdmin)