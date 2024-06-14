import email
from django import forms

from .models import *

from django.contrib.auth.models import User







class NewTaskForm(forms.ModelForm):

    class Meta:

        model = Task

        fields = ['title','text','price','image',]




class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput,
                               label='Придумайте пароль')
    
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label='Повторите пароль')

    class Meta:

        model = User

        fields = ['username','first_name','last_name','email']


    def clean_email(self):
        data = self.cleaned_data["email"]

        if User.objects.filter(email=data).exists():

            raise forms.ValidationError('Данный email уже используется')
        
        return data
    
    def clean_password2(self):

        cd = self.cleaned_data

        if cd['password'] != cd['password2']:

            raise forms.ValidationError('Пароли не совпадают')

        return cd['password2']
    
class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ['text']



class StatusInTaskForm(forms.ModelForm):

    class Meta:
        
        model = Task

        fields = ['status']