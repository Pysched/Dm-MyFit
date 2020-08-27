from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Plans
# Create your views here.


class PlanListView(ListView):
    model = Plans


class PlanDetailView(DetailView):
    model = Plans