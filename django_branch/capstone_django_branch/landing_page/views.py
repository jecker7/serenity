from django.shortcuts import render, HttpResponse, redirect
from accounts.custom_forms import RegisterUserForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def landing_page(request):
    #detect get or post
    if request.method == 'POST':
        form1 = RegisterUserForm(request.POST)
        form2 = SignUpForm(data = request.POST)
        (request.POST)
        #check if form is valid
        if form1.is_valid():
            user = form.save()
            #log the user in after
            #redirect to /home
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'landing_page/landing_page.html/', {'form1': form1, 'form2' : form2})

        if form2.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form1 = RegisterUserForm()

        form2 = SignUpForm()
    return render(request, 'landing_page/landing_page.html/', {'form1': form1, 'form2' : form2})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landing_page')
