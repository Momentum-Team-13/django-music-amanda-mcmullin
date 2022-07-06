from django import forms
from .models import Album, Favorite


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
        ]


class FavoriteForm(forms.ModelForm):
    class Meta:
        fields = [
            'user',
            'album',
        ]
        