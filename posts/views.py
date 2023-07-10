from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PostForm

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

def add_post(request):

    if request.user.is_authenticated:
        if request.method == "POST":  
            form = PostForm(request.POST)  
            if form.is_valid():  
                try:  
                    form.save() 
                    model = form.instance
                    messages.info(request, "Post has been added")
                    return redirect('index')  
                except:  
                    messages.info(request, "There was an error please try again") 
                    return render('add_post.html')
        else:  
            form = PostForm()  
        return render(request,'add_post.html',{'form':form})  
    else:
        messages.info(request, "You must logged in to add a post")
        return redirect('index')
        