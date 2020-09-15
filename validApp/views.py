from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User

# Create your views here.
def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, "index.html", context)

def signup(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect("/")