from django.shortcuts import render
from . import models


def home_page(request):
    return render(request, 'home.html')
