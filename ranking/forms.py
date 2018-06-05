from django import forms
from mastermind.models import Player

class PlayerDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlayerDataForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Player
        fields = ('player_id', 'name')
