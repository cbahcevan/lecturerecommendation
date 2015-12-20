from django import forms
from .models import TrainData

class DForms(forms.Form):
  class Meta:
       model = TrainData
       fields = ('l', 'text',)

  love = (
    (1, 'Yes'),
    (0, 'No'),)
  math = forms.ChoiceField(choices = ((1,"Yes"),(0,"No")), label="do you love math", initial='', widget=forms.Select(), required=True)
  lit = forms.ChoiceField(choices = ((1,"Yes"),(0,"No")), label="do you love literature", initial='', widget=forms.Select(), required=True)