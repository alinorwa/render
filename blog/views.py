from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def admin():
    response = redirect('admin')
    return response


def home(request):
    img = Image.objects.all()
    return render(request , 'home.html',{'imgs':img})


def about(request):
    return render(request , 'about.html')