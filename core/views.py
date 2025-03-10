from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def aboutme_view(request):
    return render(request, 'core/aboutme.html',)
