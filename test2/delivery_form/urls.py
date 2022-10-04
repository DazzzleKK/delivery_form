from django.urls import path
from .views import *

app_name = 'delivery'

urlpatterns = [
    path('', ItemList.as_view(), name='list'),
    path('create/', ItemCreate.as_view(), name='create'),
    path('delete/<int:pk>/', ItemDelete.as_view(), name='delete'),
    path('update/<int:pk>/', ItemUpdate.as_view(), name='update'),
    path('formset/', formset, name='formset'),
]
