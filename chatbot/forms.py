from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {
            'username':'',
            'email':'',
            'passwprd1':'',
            'password2':'',
        }

    def __init__(self,*args,**kwargs):
        super(CustomRegisterForm,self).__init__(*args,**kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
            self.fields[field_name].widget.attrs.update({
                'placeholder':field_name.capitalize(),
                'class':'form-control'
            })

        

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget = forms.TextInput(attrs={
            'placeholder':'Username',
            'class':'form-control'
        }),
        help_text=''
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder':'Password',
            'class':'form-control'
        }),
        help_text=''
    )