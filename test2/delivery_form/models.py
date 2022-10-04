from email.policy import default
from enum import unique
from random import choices
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator



class Choices(models.Model):
    choice = models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return f'{self.choice}'


class Item(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    delivery_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True)
    attachment = models.FileField(upload_to=None, max_length=100, blank=True)
    pickup_loc_fs = models.ManyToManyField(Choices)

    def __str__(self):
        return f'name: {self.name} type: {self.type} delivery_date: {self.delivery_date} attachment: {self.attachment} pickup_locs_fs: {self.pickup_loc_fs}'
