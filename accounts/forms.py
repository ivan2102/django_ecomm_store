from django import forms
from . models import User, UserProfile

class RegistrationForm(forms.ModelForm):

     password = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder': 'Enter Password'
     }))

     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder': 'Confirm Password'
     }))
     class Meta:
          model = User
          fields = ['first_name', 'last_name', 'email', 'password']

     def __init__(self, *args, **kwargs):
          super(RegistrationForm, self).__init__(*args, **kwargs)
          self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
          self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
          self.fields['email'].widget.attrs['placeholder'] = 'Email'
          for field in self.fields:
               self.fields[field].widget.attrs['class'] = 'form-control'

     def clean(self):
          cleaned_data = super(RegistrationForm, self).clean()
          password = cleaned_data.get('password')
          confirm_password = cleaned_data.get('confirm_password')

          if password  != confirm_password:
               raise forms.ValidationError('Password and Confirm Password does not match!')
          

class UserForm(forms.ModelForm):
     class Meta:
          model = User
          fields = ['first_name', 'last_name']

     def __init__(self, *args, **kwargs):
          super(UserForm, self).__init__(*args, **kwargs)
          for field in self.fields:
               self.fields[field].widget.attrs['class'] = 'form-control'
               

class UserProfileForm(forms.ModelForm):
     profile_picture = forms.ImageField(required=False, error_messages= {'invalid': ('Image files only')}, widget=forms.FileInput)
     class Meta:
          model = UserProfile
          fields = ('address', 'profile_picture', 'phone', 'city', 'state', 'country')

     def __init__(self, *args, **kwargs):
          super(UserProfileForm, self).__init__(*args, **kwargs)
          for field in self.fields:
               self.fields[field].widget.attrs['class'] = 'form-control'
          
               