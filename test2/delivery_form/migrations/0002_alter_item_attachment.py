# Generated by Django 4.0 on 2022-10-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='attachment',
            field=models.FileField(blank=True, upload_to=None),
        ),
    ]