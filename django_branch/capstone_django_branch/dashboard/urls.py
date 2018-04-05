from django.conf.urls import url
#importing views from all base level views files
from . import views

urlpatterns = [
    #setting our url pattern to just the end of our string, accounts
    url(r'^$', views.dashboard, name = "dashboard"),
]
