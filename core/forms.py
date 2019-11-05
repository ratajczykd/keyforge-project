from django import forms
from core.models import Player

class NameForm(forms.ModelForm):
    name = forms.CharField(label='Player name', max_length=100)

    class Meta:
        model = Player
        fields = {'name',}
