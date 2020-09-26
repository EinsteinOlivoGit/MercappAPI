from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from purchase.models import Item
from purchase.forms import itemForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ItemList(ListView):
    model = Item
    template_name = 'item/list.html'
    context_object_name = 'items'

class ItemCreate(CreateView):
    model = Item
    form_class = itemForm
    template_name = 'item/form.html'
    success_url = reverse_lazy('purchase:item_list')

class ItemUpdate(UpdateView):
    model = Item
    form_class = itemForm
    template_name = 'item/form.html'
    success_url = reverse_lazy('purchase:item_list')