# Owner Daine.H
# Modify 2016-01-05

from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^login/$', views.login_page, name='login_page'),


]