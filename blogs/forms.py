from django.db import models
from django import forms

class BLOGENTRY(forms.Form):
	title=forms.CharField()
	blog=forms.CharField(widget=forms.Textarea)
	name=forms.CharField()
	email=forms.EmailField()

