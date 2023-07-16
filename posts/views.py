from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        

        if password1 == password2:

            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.warning(request, 'Username has already been used')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
                user.save()
                login(request, user)
                messages.info(request, "Your account has been successfully created")
                return redirect('index')
            
        else:
            messages.info(request, 'Password do not match')
            return redirect('register')
        
    return render(request, 'register.html')

def add_post(request):

    if request.user.is_authenticated:
        if request.method == "POST":  
            form = PostForm(request.POST)  
            if form.is_valid():  
                try:  
                    item = form.save(commit=False)
                    item.author = request.user
                    item.save()
                    messages.info(request, "Post has been added")
                    return redirect(f'post/{item.id}')  
                except:  
                    messages.info(request, "There was an error please try again") 
                    return redirect('add_post')
        else:  
            form = PostForm()  
        return render(request,'add_post.html',{'form':form})  
    else:
        messages.info(request, "You must logged in to add a post")
        return redirect('index')
    

@login_required(login_url="login")
def update_post(request, pk):
    post = Post.objects.get(id=pk)
 
    form = PostForm(request.POST or None, instance=post)  
    if form.is_valid():  
        try:  
            form.save() 
            model = form.instance
            messages.info(request, "Your post has been updated")
            return redirect('index')  
        except Exception as e: 
            messages.info(request, "There was an error. Please try again")   
            return redirect('update_post') 
    return render(request,'update_post.html',{'form':form, 'post':post})  


@login_required(login_url="login")
def delete_post(request, pk):

    post = Post.objects.get(id=pk)

    if request.user.id == post.author.id:

        post.delete()

        messages.info(request, "Your post has been deleted")
        return redirect('index')
    else:
        messages.warning(request, "You tried to delete a post which does not belong to you! Please do not attempt this again.")
        return redirect('index')
        

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect('index')


def liked_view(request):
    pass
