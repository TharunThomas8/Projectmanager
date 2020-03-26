from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Cards,Chat

class NewCard(forms.ModelForm):
	class Meta:
		model = Cards
		fields = ['title','description','due','assigned']
		widgets = {
            'due': DatePickerInput(), # specify date-frmat
        }

class NewChat(forms.ModelForm):
	class Meta:
		model = Chat
		fields = ['author','msg','card']