from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        CLASS_VAR = " px-3 py-2 w-full rounded-xl bg-gray-600 text-white border border-teal-500 shadow-md"
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "message": forms.Textarea(attrs={
                "placeholder":"type your message...",
                "class": f"{CLASS_VAR} h-28 resize-none align-top",
                "id":"message"
            }),
            
            "name": forms.TextInput(attrs={
                "placeholder": "Enter your name",
                "id": "name",
                "class": CLASS_VAR,
            }),
            
            "email": forms.EmailInput(attrs={
                "placeholder": "email adress",
                "id": "email",
                "class": CLASS_VAR
            })
        }
    
        
        