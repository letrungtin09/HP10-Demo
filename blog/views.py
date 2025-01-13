from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


