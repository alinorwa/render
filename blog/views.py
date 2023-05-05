from django.shortcuts import redirect, render


# Create your views here.
def admin():
    response = redirect('admin')
    return response


def home(request):
    return render(request , 'home.html')


def about(request):
    return render(request , 'about.html')