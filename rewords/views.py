from django.shortcuts import render
from django.http import request,HttpResponse
from . import models
from django.db.models import Sum

# Create your views here.
def index(request):
    return render(request,'reword.html')


def get_reword(request):
    pass