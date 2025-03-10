from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success_view")
    else:
        form = ContactForm()
        
    return render(request, 'contact/contact.html', {"form":form})


def success_view(request):
    return render(request, 'contact/success.html')
