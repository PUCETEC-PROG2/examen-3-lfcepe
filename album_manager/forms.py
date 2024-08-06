from django import forms
from .models import Artist, Album

class Artist_Form(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'artist_name': forms.TextInput (attrs={'class': 'form-control'}),
            'artist_country': forms.TextInput (attrs={'class': 'form-control'}),
            'artist_biography': forms.TextInput (attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput (attrs={'class': 'form-control-file'}),
        }

class Album_Form(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_title': forms.TextInput (attrs={'class': 'form-control'}),
            'year': forms.TextInput (attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'album_details': forms.TextInput (attrs={'class': 'form-control'}),
            'covers': forms.ClearableFileInput (attrs={'class': 'form-control-file'}),
        }