from django.shortcuts import render, HttpResponse, redirect
from accounts.custom_forms import RegisterUserForm
from accounts.custom_forms import SignUpForm
from django.contrib.auth import login

def signup_view(request):
    #detect get or post
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        (request.POST)
        #check if form is valid
        if form.is_valid():
            user = form.save()
            #log the user in after
            #redirect to /home
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/signup.html/', {'form':form})
    #if get, return a blank form
    else:
        form = RegisterUserForm()
    return render(request, 'accounts/signup.html/', {'form':form})

def login_view (request):
    if request.method == 'POST':
        form = SignUpForm(data= request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landing_page')
