from django.conf.urls import url
from django.urls import path
#importing views from all base level views files
from . import views

urlpatterns = [
    #setting our url pattern to just the end of our string, accounts
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name ="login"),
    path("fancy_signup/", views.fancy_signup_view, name = "fancy_signup"),
    path("fancy_signup2/", views.fancy_signup_view2, name = "fancy_signup2")
]
