from django.conf.urls import url
from django.urls import path
#importing views from all base level views files
from . import views

urlpatterns = [
    #setting our url pattern to just the end of our string, accounts
    path('', views.home, name="home"),

]
