from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "message": forms.Textarea(attrs={
                "placeholder": "Type your message...",
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300 resize-none",
                "id": "message",
                "rows": "6"
            }),
            
            "name": forms.TextInput(attrs={
                "placeholder": "Enter your full name",
                "id": "name",
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300"
            }),
            
            "email": forms.EmailInput(attrs={
                "placeholder": "Enter your email address",
                "id": "email", 
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-300"
            })
        }