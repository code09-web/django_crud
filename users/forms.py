from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserModels

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = UserModels
		fields = ['name', 'email', 'password']
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})
		}
