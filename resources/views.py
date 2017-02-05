import account.views
import base64
import hashlib
import pprint as pp
import os
import uuid

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.generic import TemplateView

from .models import Resource, Item, Storage
from .forms import ResourceForm, ItemForm, GroupForm, DeleteForm
from .encryption import symEncrypt_b64, symDecrypt_b64



def getSymKey_b64(password, salt):
    bin_salt = base64.b64decode(salt)
    bin_pass = hashlib.sha256(password.encode('utf-8')).digest()
    bk = hashlib.pbkdf2_hmac('sha256', bin_pass, bin_salt, 100000)
    return base64.b64encode(bk).decode('ascii')


class HomeView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/resources/groups')
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
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = Resource(name=form.cleaned_data["name"],
                    url=form.cleaned_data["url"], group_id=group.id)
            resource.save()
            return HttpResponseRedirect('/resources/groups/{}'.format(group.id))
    form = ResourceForm()
    resources = group.resource_set.all()
    context = {"form": form, "group": group, "resources": resources}
    return render(request, "groups/detail.html", context)


@login_required(login_url='/account/login/')
def groups_delete(request, group_id):
    if not request.user.groups.filter(pk=group_id).exists():
        raise Http404
    group = get_object_or_404(Group, pk=group_id)
    storage = get_object_or_404(Storage, group_id=group_id)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            group.delete()
            return HttpResponseRedirect("/resources/groups/")
    form = DeleteForm()
    context = {"issue": storage.name, "form": form}
    return render(request, "delete.html", context)


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
    if not request.user.groups.filter(pk=resource.group_id).exists():
        raise Http404
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


def delete_resource(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    if not request.user.groups.filter(pk=resource.group_id).exists():
        raise Http404
    group_id = resource.group_id
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            resource.delete()
            return HttpResponseRedirect("/resources/groups/{}".format(group_id))
    form = DeleteForm()
    context = {"resource": resource, "form": form}
    return render(request, "resources/delete.html", context)


def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    resource = item.resource
    if not request.user.groups.filter(pk=resource.group_id).exists():
        raise Http404
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            item.delete()
            return HttpResponseRedirect("/resources/{}".format(resource.pk))
    form = DeleteForm()
    context = {"item": item, "form": form}
    return render(request, "items/delete.html", context)


