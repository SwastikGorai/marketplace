from django import forms
from .models import Conversation, ConversationMessage


class ConverstaionMessageForm(forms.ModelForm):
    
    class Meta:
        model = ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(attrs={
                "class" : "w-full py-4 px-6 rounded-2xl border"
                }),
        }
