from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


from django.contrib import admin

from resources.views import SignupView, LoginView, HomeView


urlpatterns = [
    #url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^account/login/$", LoginView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),
    url(r"^favicon.ico$", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"), permanent=False), name="favicon"),
    url(r"^resources/", include("resources.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
