from django import forms
from mastermind.models import Player

class PlayerDataForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('player_id', 'name')
