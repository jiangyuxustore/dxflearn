# Generated by Django 4.0.8 on 2023-03-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='主键订单号'),
        ),
        migrations.AlterModelTable(
            name='order',
            table='order_info',
        ),
    ]
