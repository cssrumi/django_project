from django import forms
from products.models import Product, Provider


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('provider', 'title', 'description', 'price')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ('name', 'description', 'location')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }
