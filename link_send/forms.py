from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import Email
from link_send.models import Email

# class EmailForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = Email
#         fields = ('email')


class EmailForm(forms.ModelForm):
	class Meta:
		model = Email
		fields = '__all__'
		exclude = ['slug','created_at','updated_at']

