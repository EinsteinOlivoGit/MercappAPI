from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from purchase.models import Item

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ItemList(ListView):
    model = Item
    template_name = 'item/list.html'
    context_object_name = 'items'