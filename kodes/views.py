from re import template
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic


from django.templatetags.static import static

import requests
import json
import os

from .models import Empresa, Usuario
from .forms import EmpresaForm

class Home(generic.ListView):
    model = Empresa
    template_name = "home.html"
    context_object_name = "obj"
    form_class = EmpresaForm





    def __init__(self):
        #u = Usuario.objects.get(username__exact='carlosmartinez')
        #u.set_password("kodes79@")
        #u.save()
        print("Inicio......")
    
        #auth_token='2cde7694-b99b-426e-b13a-d7648d7bb48f'
        #auth_token='1gAwwGYR8DEpyTWwyf3HxqvOCK2iIh8j7PvIQOHsrqJ2f61AbBeWTV7FZqKA94hMfb0'
        #hed = {'Authorization': 'Bearer ' + auth_token, 'Accept': 'application/json'}
        #data = {'app' : 'aaaaa'}
        #url = 'https://www.universal-tutorial.com/api/countries/'
        #response = requests.post(url, headers=hed)
        #print(response)
        #response.raise_for_status()  # raises exception when not a 2xx response
        #response.headers["content-type"].strip().startswith("application/json")
        #if response.status_code != 204:
        #    print(response.json())
        
        ##file_countries = os.path.abspath(os.getcwd())+'/kodes/static/json/countries.json'
        ##file_states = os.path.abspath(os.getcwd())+'/kodes/static/json/states.json'
        ##file_cities = os.path.abspath(os.getcwd())+'/kodes/static/json/cities.json'
        
        ##with open(file_countries, 'r', encoding='utf8') as j:
        ##    countries = json.loads(j.read())
        ##with open(file_states, 'r', encoding='utf8') as j:
        ##    states = json.loads(j.read())
        ##with open(file_cities, 'r', encoding='utf8') as j:
        ##    cities = json.loads(j.read())
                    

class EmpresaNew(generic.CreateView):
    model = Empresa
    template_name = "empresa_new.html"
    context_object_name = "obj"
    form_class = EmpresaForm
    success_url = reverse_lazy("home")


    
            
  