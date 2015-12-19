from django import forms
class DForms(forms.Form):

 love = (
    (1, ‘Yes’),
    (0, ’No’),
)
math = forms.ChoiceField(choices = love, label="", initial='', widget=forms.Select(), required=True)
