from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Item
from django.urls import reverse, reverse_lazy
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import modelformset_factory
from django.forms.widgets import CheckboxSelectMultiple

# Create your views here.


def home_view(request):
    return render(request, 'delivery_form/delivery.html')


class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('delivery:list')
    widgets = {'delivery_date': AdminDateWidget(attrs={'type': 'date'})}

    def get_form(self, form_class=None):
        form = super(ItemCreate, self).get_form(form_class)
        form.fields['delivery_date'].widget = AdminDateWidget(
            attrs={'type': 'date'})
        return form


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
    ItemFormSet = modelformset_factory(Item, fields=('name', 'type', 'delivery_date', 'attachment', 'pickup_loc_fs'), widgets={
                                       'delivery_date': AdminDateWidget(attrs={'type': 'date'}), 'pickup_loc_fs': CheckboxSelectMultiple()}, extra=2)
    formset = ItemFormSet()

    if request.method == 'POST':
        formset = ItemFormSet(request.POST)
        instances = formset.save()

    return render(request, 'delivery_form/item_form.html', {'form': formset})
