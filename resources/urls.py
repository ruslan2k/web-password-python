from django.conf.urls import url

from . import views

urlpatterns = [
    # /resources/
    url(r'^$', views.index, name='resources_index'),
    url(r'^(?P<resource_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<resource_id>[0-9]+)/delete/$', views.delete_resource, name='delete_resource'),
    url(r'^item/(?P<item_id>[0-9]+)/delete/$', views.delete_item, name='delete_item'),
    url(r'^groups/$', views.groups_index, name='groups_index'),
    url(r'^groups/(?P<group_id>[0-9]+)/$', views.groups_detail, name='groups_detail'),
    # /resources/test/
    #`url(r'^test/$', views.test, name='test'),
]

