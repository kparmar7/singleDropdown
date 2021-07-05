from django.shortcuts import render
from .forms import IntegerFieldForm
import logging

from .forms2 import *
from .models2 import *

def FormViewData(req):
    form = IntegerFieldForm(req.GET)
    print('Data from FORM submit',req.GET, req.method)
    logging.info(  "------------DataFlair Logging Tutorials")
    if req.GET.get('charField') != None:
        fm = IntegerFieldForm(req.GET)
        if fm.is_valid():
            print('Data from FORM submit--', req.GET['charField'])
            print('DATA --', fm.cleaned_data['charField'])
            print('DATA --', fm.cleaned_data.get('charField'))
            print('DATA --', fm.data['charField'])
            print('DATA --', fm.data)
            return render(req, 'form.html', {'FORM': fm})
    return render(req, 'form.html', {'FORM':form})


def List(req):
    form = CountriesForm(initial={'name':'India'})
    if req.POST.get('name') != None:
        country_id = Countries.objects.values_list('id', flat=True).filter(name=req.POST.get('name'))
        data = States.objects.filter(country=country_id[0])
        form = CountriesForm(initial={'name': req.POST.get('name')})
        return render(req, 'LIST.html', {'DATA':data, 'FORM': form})
    return render(req, 'LIST.html', {'FORM': form})
