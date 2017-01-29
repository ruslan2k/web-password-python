from django import forms


class ResourceForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    url  = forms.CharField(label='url',  max_length=250, required=False)


class DeleteResourceForm(forms.Form):
    pass


class ItemForm(forms.Form):
    item_key = forms.CharField(label='key', max_length=100)
    item_val = forms.CharField(label='val', max_length=100)
    #item_url = forms.CharField(label='url', max_length=250, required=False)


class DeleteItemForm(forms.Form):
    pass


class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', max_length=100)
