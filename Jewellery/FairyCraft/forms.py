from .models import *
from django.forms import ModelForm
from django import forms
#Формы для обработки HTML запросов 

class JewelleryForm(ModelForm):

    class Meta:
        model = Jewellery
        fields = ('jewellery_name', 'jewellery_price', 'jewellery_img')


class LoginForm(forms.Form):
    mail_address = forms.EmailField(label='Email')
    us_password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    mail_address = forms.EmailField(label='Email')
    us_password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    us_surname = forms.CharField(label='Фамилия')
    us_name = forms.CharField(label='Имя')
    phone_num = forms.CharField(label='Телефон')
    us_img = forms.ImageField(label='Фото', required=False)