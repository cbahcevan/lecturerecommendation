from django import forms
from .models import TrainData

class DForms(forms.Form):
  class Meta:
       model = TrainData
       fields = ('l', 'text',)

  love = (
    (1, 'Yes'),
    (0, 'No'),)
  math = forms.ChoiceField(choices = ((1,"Yes"),(0,"No")), label="do you love solving problems", initial='', widget=forms.Select(), required=True)
  read = forms.ChoiceField(choices = ((1,"Yes"),(0,"No")), label="do you love reading", initial='', widget=forms.Select(), required=True)
  lit = forms.ChoiceField(choices = ((1,"Yes"),(0,"No")), label="do you love literature", initial='', widget=forms.Select(), required=True)
  high = forms.ChoiceField(choices = ((1,"Yes"),(0,"No")), label="do you still love your high school lectures ?", initial='', widget=forms.Select(), required=True)
  music = forms.ChoiceField(choices = ((1,"Yes"),(0,"No")), label="do you love music", initial='', widget=forms.Select(), required=True)
  politics = forms.ChoiceField(choices = ((1,"Yes"),(0,"No")), label="do you interested in politics", initial='', widget=forms.Select(), required=True)