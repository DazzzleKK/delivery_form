# Generated by Django 4.0 on 2022-10-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_form', '0005_remove_item_pickup_loc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='delivery_date',
            field=models.DateField(null=True),
        ),
    ]
