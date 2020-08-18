from django import forms
from .models import Account,Contact
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={ 'placeholder':'Password'}))
    password2 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={ 'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('username','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(RegistrationUserForm, self).__init__(*args, **kwargs)
       
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=False,  max_length=254,widget=forms.EmailInput(attrs={ 'placeholder':'Email'}))
   # name = forms.CharField(label='Your name')
    
    class Meta:
        model = Account
        fields = ('email','contact')

        widgets = {
            'contact': forms.TextInput(attrs={'placeholder': 'ex: +9999999999'}),
        }

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']

            if "@" not in email:
                raise forms.ValidationError("Enail not valid")
            if Account.objects.filter(email=email).exists():
                raise forms.ValidationError("Email Id alreay exists")


            


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    class Meta:
        model = Account
        fields = ( 'name','password')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        }

    # def clean(self):
    #     if self.is_valid():
    #         name = self.cleaned_data['name']
    #         if not Account.objects.filter(name=name).exists():
    #             if not Account.objects.filter(email=name).exists():
    #                 raise forms.ValidationError("name not valid")


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = ( 'name','password')
        fields = ('name','contact','city','message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'contact': forms.TextInput(attrs={'placeholder': '+919876543210'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message',"rows":2, "cols":32}),
        }