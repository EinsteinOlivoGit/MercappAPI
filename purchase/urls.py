from django.urls import path 
from purchase.views import index, ItemList, ItemCreate, ItemUpdate

app_name = 'purchase'
urlpatterns = [
    path('', index, name='index'),
    path('item', ItemList.as_view(), name='item_list'),
    path('item/create', ItemCreate.as_view(), name='item_create'),
    path('item/edit/<int:pk>', ItemUpdate.as_view(), name='item_edit')
]
