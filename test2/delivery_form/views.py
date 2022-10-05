from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Item
from django.urls import reverse, reverse_lazy
from django.contrib.admin.widgets import AdminDateWidget
from .forms import ItemForm, ItemFormSet
from django.forms.widgets import CheckboxSelectMultiple
# Create your views here.


class ItemCreate(CreateView):
    model = Item
    success_url = reverse_lazy('delivery:list')
    form_class = ItemForm

    

class ItemList(ListView):
    model = Item


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('delivery:list')


class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('delivery:list')


def formset(request):  
    formset = ItemFormSet()
    if request.method == 'POST':
        formset = ItemFormSet(request.POST)
        formset.save()

    return render(request, 'delivery_form/item_form.html', {'formset': formset})
