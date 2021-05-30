from django import forms

class TickerForm(forms.Form):
	ticker = forms.CharField(label='ticker',max_length=5)