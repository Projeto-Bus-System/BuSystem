from django import forms
from .models import Map, Bookmarks



class AddPointsMap(forms.ModelForm):
    class Meta:
        model = Map
        fields = '__all__'


class AddMap(forms.ModelForm):
    class Meta:
        model = Bookmarks
        fields = '__all__'
