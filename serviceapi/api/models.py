from django.db import models
from django.urls import reverse
# Create your models here.


class Ticket(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заказ')
    price_dlr = models.DecimalField(max_digits=10, decimal_places=2)
    deliv_data = models.CharField(max_length=250, verbose_name='Cрок поставки')
    price_in_ru = models.DecimalField(max_digits=10, decimal_places=2)
    delivered = models.BooleanField(default=False, verbose_name='Доставлено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['-deliv_data']
