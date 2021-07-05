from django.forms import ModelForm
from .models2 import *
from django import forms

class CountriesForm(ModelForm):
    name = forms.ModelChoiceField(queryset=Countries.objects.values_list('name', flat=True), label='select Country Name')

    class Meta:
        model = Countries
        fields = ['name']

class StatesForm(ModelForm):
    name = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING)

    class Meta:
        model = States
        fields = ['name', 'country']
