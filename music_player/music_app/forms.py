
from django import forms
from crispy_forms.helper import FormHelper
from django.forms.models import inlineformset_factory
from crispy_forms.layout import Layout,Field, Fieldset, ButtonHolder, Submit,Button, Div
from django.forms import CharField, Form, PasswordInput
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
import requests
from music_app.models import Song,Video

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Enter Email or Number")
    password =  forms.CharField(widget=PasswordInput())

    def __init__(self,*args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)



    def clean(self):
        user_name = self.cleaned_data['user_name']
        password = self.cleaned_data['password']
        print(user_name,password,'bala')
        if user_name and password:
            user = authenticate(username=user_name, password=password)
            print(user)
            if user:
            #     if user.is_superuser:
            #         login(request, user)
                print('login')
            else:
                print('error')
                raise forms.ValidationError('')
        return user    






class SongForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        # self.fields['title'].required = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
           Div(
                Div(Field('title'), css_class="col-md-6"),

                css_class='row'
            ), 
             Div(
                Div(Field('description'), css_class="col-md-6"),
                css_class='row'
            ), 
            Div(
                Div(Field('music'), css_class="col-md-6"),
                css_class='row'
            ),        
       		            Div(
                Div(Field('artist'), css_class="col-md-6"),
                css_class='row'
            ),
                        Div(
                Div(Field('poster'), css_class="col-md-6"),
                css_class='row'
            ), 
        )

    def clean(self):
        music = self.cleaned_data.get('title')
        if music:
            print('music file is comming')
            print(music)
    class Meta:
        # model = models.Song
        model = Song
        fields =(
        'title',
        'description',
        'music',
        'artist',
        'poster',
        )





class VideoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        # self.fields['title'].required = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
           Div(
                Div(Field('title'), css_class="col-md-6"),

                css_class='row'
            ), 
             Div(
                Div(Field('description'), css_class="col-md-6"),
                css_class='row'
            ), 
            Div(
                Div(Field('video'), css_class="col-md-6"),
                css_class='row'
            ),        
                        Div(
                Div(Field('artist'), css_class="col-md-6"),
                css_class='row'
            ),
                        Div(
                Div(Field('poster'), css_class="col-md-6"),
                css_class='row'
            ), 
        )

    def clean(self):
        music = self.cleaned_data.get('music')
        if music:
            print('music file is comming')
            print(music)
    class Meta:
        # model = models.Song
        model = Video
        fields =('title',
        'description',
        'video',
        'artist',
        'poster',
        )