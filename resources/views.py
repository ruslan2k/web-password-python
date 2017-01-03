import account.views
import base64
import hashlib
import pprint as pp
import os
import uuid

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.generic import TemplateView

from .models import Resource, Item, Storage
from .forms import ResourceForm, ItemForm, DelItemForm, GroupForm
from .encryption import symEncrypt_b64, symDecrypt_b64



def getSymKey_b64(password, salt):
    bin_salt = base64.b64decode(salt)
    bin_pass = hashlib.sha256(password.encode('utf-8')).digest()
    bk = hashlib.pbkdf2_hmac('sha256', bin_pass, bin_salt, 100000)
    return base64.b64encode(bk).decode('ascii')


class HomeView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/resources')
        return render(request, 'homepage.html')


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


@login_required(login_url='/account/login/')
def groups_index(request):
    groups = request.user.groups.all()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = Group.objects.create(name=str(uuid.uuid4()))
            group.user_set.add(request.user)
            group.save()
            name = form.cleaned_data["group_name"]
            storage = Storage(group_id=group.id, name=name)
            storage.save()
            return HttpResponseRedirect('/resources/groups')
    else:
        form = GroupForm()
    context = {"groups": groups, "form": form}
    return render(request, "groups/index.html", context)


@login_required(login_url='/account/login/')
def groups_detail(request, group_id):
    return HttpResponse(group_id)


def test(request):
    response = 'test<br>'
    if 'sym_key' in request.session:
        response += 'sym_key - exists'
        #print(request.session['sym_key'])
    else:
        response += 'sym_key - NOT exists'
    return render(request, "test/page.html")


@login_required(login_url='/account/login/')
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ResourceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #pp.pprint(form.cleaned_data)
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
    sym_key = request.session['sym_key']
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item(resource_id=resource_id)
            item.key = symEncrypt_b64(sym_key, form.cleaned_data["item_key"])
            item.val = symEncrypt_b64(sym_key, form.cleaned_data["item_val"])
            item.save()
            return HttpResponseRedirect("/resources/{}/".format(resource_id))
    else:
        form = ItemForm()
        items = map(lambda i: decryptItem(sym_key, i), resource.item_set.all())
    context = {"resource": resource, "form": form, "items": items}
    return render(request, "resources/detail.html", context)


def decryptItem(key_b64, item):
    return {
            'pk': item.id,
            'key': symDecrypt_b64(key_b64, item.key),
            'val': symDecrypt_b64(key_b64, item.val),
    }


def delete_item(request):
    pass
