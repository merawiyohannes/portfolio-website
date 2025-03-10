from django.shortcuts import render

def adress_view(request):
    return render(request, 'adress/adress.html')
