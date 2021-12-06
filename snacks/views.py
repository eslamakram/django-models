
from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack


# Create your views here.

class SnackListView(ListView): 
    template_name = "snack_list.html"
    Model = Snack

    def get_queryset(self):
        return Snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    Model = Snack

    def get_queryset(self):
        return models.Snack