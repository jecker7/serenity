from django.shortcuts import render

# Create your views here.
def mood(request):
    return render(request, 'mood/mood.html')
