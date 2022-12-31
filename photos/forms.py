from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(forms.ModelForm):
     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg mb-3'}), max_length=30, required=True)
     email = forms.CharField(
        widget=forms.EmailInput(attrs={'class':'form-control mb-3'}), max_length=100, required=True)
     password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control mb-3 form-control-lg'}), required=True)
     confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}), required=True)


     class Meta:
        model = User
        # message = forms.CharField(widget=CKEditorUploadingWidget())
        fields = ( 'email', 'username', 'password')



     def clean(self):
         super(SignupForm, self).clean()
         password = self.cleaned_data.get('password')
         username = self.cleaned_data.get('username')
         email = self.cleaned_data.get('email')
         
         confirm_password = self.cleaned_data.get('confirm_password')

         # overiding the clean function to make sure password is validate
         if password != confirm_password:
            self._errors['password'] = self.error_class('Password do not match try again')


         forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'master', 'administrator', 
         'root', 'email', 'user', 'join', 'static', 'python']

         if username.lower() in forbidden_users:
            self._errors['username'] = self.error_class('The username you have used is a reserved word...')
         
         if User.objects.filter(email__iexact=email).exists():
            self._errors['email'] = self.error_class('User with this email already exists.')


         return self.cleaned_data