from django import forms
from .models import Ad

# Form for creating and editing ads
class AdForm(forms.ModelForm):
    class Meta:
        model = Ad # Use the Ad model
        fields = ['title', 'content', 'is_active', 'revenue'] # Fields to include in the form
