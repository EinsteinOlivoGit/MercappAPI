from django.urls import path 
from purchase.views import index, ItemList

urlpatterns = [
    path('', index, name='index'),
    path('item', ItemList.as_view(), name='item_list'),
]
