from django.shortcuts import render, HttpResponse

def landing_page(request):
    return render(request, 'landing_page/landing_page.html')
