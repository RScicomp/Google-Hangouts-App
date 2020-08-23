from django.db import models
from django import forms
# Create your models here.
LENGTH_CHOICES = [(0.1,0.1),(0.25,0.25),(0.5,0.5),(0.75,0.75),(0.85,0.85),(0.95,0.95)]
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Summaryform(forms.Form):
    data = forms.CharField(label='To Summarize :', max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Text', 'class':'input'}))

class Schedulingform(forms.Form):
    advisorno = forms.IntegerField(widget = forms.TextInput(attrs = {'class':'input'}))
    startupno = forms.IntegerField(widget = forms.TextInput(attrs = {'class':'input'}))
    timeslotno = forms.IntegerField(widget = forms.TextInput(attrs = {'class':'input'}))
    groupsize = forms.IntegerField(widget = forms.TextInput(attrs = {'class':'input'}))
class Movieform(forms.Form):
    movie_type = forms.CharField(label='Movie Type :', max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Text', 'class':'input'}))
    movie_name = forms.CharField(label='Movie Name :', max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Text', 'class':'input'}))
class Hangoutsform(forms.Form):
    link = forms.CharField(label='Room Link :', max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Text', 'class':'input'}))
    name = forms.CharField(label='Room Name :', max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Text', 'class':'input'}))
    password = forms.CharField(label='Password :', required=False, max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Text', 'class':'input'}))

class Roomform(forms.Form):
    toenter=""
    roomurl=""
    password = forms.CharField(label='Password :', required=False, max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Text', 'class':'input'}))
    
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
class UploadFileForm(forms.Form):
    file = forms.FileField()
    