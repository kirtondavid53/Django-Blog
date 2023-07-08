from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts' : posts })

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'post' : post })

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "You have successfully logged in")
            return redirect('index')

        else:
            messages.info(request, "Invalid credentials, Please try again")
            return redirect('login')
            

    return render(request, 'login.html')
