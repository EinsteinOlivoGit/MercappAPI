from django import forms
from purchase.models import Item
from datetime import datetime
class itemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = [
            'name',
            'brand',
            'create_date',
            'last_update_date',
            'users',
            'state'
        ]
        labels = {
            'name': 'Name',
            'brand': 'Brand',
            'create_date': 'Create date',
            'last_update_date': 'Last update',
            'users': 'Users',
            'state': 'State'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.TextInput(attrs={'class':'form-control'}),
            'create_date': forms.DateInput(format='%m/%d/%Y', attrs={'class':'form-control','value': datetime.now().strftime("%m/%d/%Y")}),
            'last_update_date': forms.DateInput(format='%m/%d/%Y', attrs={'class':'form-control','value': datetime.now().strftime("%m/%d/%Y")}),
            'users': forms.CheckboxSelectMultiple(),
            'state': forms.TextInput(attrs={'class':'form-control'})
        }