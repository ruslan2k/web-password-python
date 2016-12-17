import account.views
import base64
import hashlib
import pprint as pp
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Resource, Item
from .forms import ResourceForm, ItemForm, DelItemForm


def getSymKey_b64(password, salt):
    bin_salt = base64.b64decode(salt)
    bin_pass = hashlib.sha256(password.encode('utf-8')).digest()
    bk = hashlib.pbkdf2_hmac('sha256', bin_pass, bin_salt, 100000)
    return base64.b64encode(bk).decode('ascii')


class SignupView(account.views.SignupView):

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

    def update_profile(self, form):
        print('update_profile')
        password = form.cleaned_data['password']
        salt = self.created_user.profile.salt
        sym_key = getSymKey_b64(password, salt)
        if 'sym_key' in self.request.session:
            print('secret exists')
        else:
            print('secret NOT exists')
        self.request.session['sym_key'] = sym_key


class LoginView(account.views.LoginView):

    def after_login(self, form):
        self.update_session(form)
        super(LoginView, self).after_login(form)

    def update_session(self, form):
        print('update_session')
        if not self.request.user.is_authenticated():
            return
        password = form.cleaned_data['password']
        salt = self.request.user.profile.salt
        sym_key = getSymKey_b64(password, salt)
        if 'sym_key' in self.request.session:
            print('secret exists')
        self.request.session['sym_key'] = sym_key


def test(request):
    response = 'test<br>'
    if 'sym_key' in request.session:
        response += 'sym_key - exists'
        print(request.session['sym_key'])
    else:
        response += 'sym_key - NOT exists'
    return HttpResponse(response)


@login_required(login_url='/account/login/')
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ResourceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pp.pprint(form.cleaned_data)
            resource = Resource(name=form.cleaned_data["resource_name"], user_id=request.user.id)
            resource.save()
            return HttpResponseRedirect('/resources')
    else:
        form = ResourceForm()
    resources = request.user.resource_set.all()
    context = {"resources": resources, "form": form}
    return render(request, "resources/index.html", context)


@login_required(login_url='/account/login/')
def detail(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item(key=form.cleaned_data["item_key"], val=form.cleaned_data["item_val"],
                    resource_id=resource_id)
            item.save()
            return HttpResponseRedirect("/resources/%s/" % resource_id)
    else:
        form = ItemForm()
    context = {"resource": resource, "form": form}
    return render(request, "resources/detail.html", context)

def delete_item(request):
    pass
