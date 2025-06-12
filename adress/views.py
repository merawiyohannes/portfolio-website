from django.shortcuts import render

def adress_view(request):
    return render(request, 'adress/adress.html')

def myprojects_view(request):
    return render(request, 'adress/projects.html')