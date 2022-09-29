# Generated by Django 4.1.1 on 2022-09-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заказ')),
                ('price_dlr', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creat_content', models.DateTimeField(auto_now_add=True, verbose_name='Cрок поставки')),
                ('price_in_ru', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Delivered', models.BooleanField(default=False, verbose_name='Доставлено')),
            ],
        ),
    ]
