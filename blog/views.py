from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def admin():
    response = redirect('admin')
    return response


def home(request):
    img = Image.objects.all()
    posts = Post.objects.all()
    context = {'imgs':img , 'posts':posts}
    return render(request , 'home.html',context)


def about(request):
    return render(request , 'about.html')