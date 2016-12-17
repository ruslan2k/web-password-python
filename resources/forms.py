from django import forms


class ResourceForm(forms.Form):
    resource_name = forms.CharField(label='Resource name', max_length=100)


class ItemForm(forms.Form):
    item_key = forms.CharField(label='key', max_length=100)
    item_val = forms.CharField(label='val', max_length=100)


class DelItemForm(forms.Form):
    pass
