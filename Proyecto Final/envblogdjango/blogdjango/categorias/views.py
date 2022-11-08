from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categorias

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms

# Create your views here.

class ListadoCategorias(ListView):
    model = Categorias

class Primerab(TemplateView):
    template_name = "primerab.html"

class Error(TemplateView):
    template_name = "error.html"