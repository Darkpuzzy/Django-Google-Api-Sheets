# Generated by Django 4.1.1 on 2022-10-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_ticket_deliv_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-deliv_data'], 'verbose_name': 'Order', 'verbose_name_plural': 'Order'},
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='title',
            new_name='order',
        ),
    ]
