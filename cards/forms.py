from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Cards

class NewCard(forms.ModelForm):
	class Meta:
		model = Cards
		fields = ['title','description','due','assigned']
		widgets = {
            'due': DatePickerInput(), # specify date-frmat
        }