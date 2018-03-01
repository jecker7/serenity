from django.conf.urls import url
from django.urls import path
#importing views from all base level views files
from . import views

urlpatterns = [
    #setting our url pattern to just the end of our string, accounts
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name ="login")
]
