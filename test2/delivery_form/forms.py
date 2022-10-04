from django import forms
from .models import Item
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import CheckboxSelectMultiple


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {'delivery_date': AdminDateWidget(
            attrs={'type': 'date'}), 'pickup_loc_fs': CheckboxSelectMultiple()}
