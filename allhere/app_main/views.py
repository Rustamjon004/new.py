

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from app_main.forms import PostForm
from app_main.models import Post


# Create your views here.
@login_required(login_url="/users/login/")
def home_page(request):
    return render(request, "app_main/home.html")


@login_required(login_url="/users/login/")
def users_page(request):

    if not request.user.is_superuser:
        return redirect("/")

    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "app_main/users.html", context)
@login_required(login_url="/users/login/")
def my_posts(request):
    my_posts = Post.objects.filter(owner=request.user)

    context = {
        'my_posts': my_posts
    }
    return render (request,'app_main/my_posts.html',context)

@login_required(login_url="/users/login/")
def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            messages.success(request, 'kiritilgan malumotlar post qilib yaratildi!')
            return redirect("/")
        else:
            messages.error(request, 'malumotlar kiritilmadi!')
            return redirect("/new-post")

    context = {
        'form': form
    }
    return render(request, 'app_main/new_post.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    context = {
        'post': post,
    }
    return render(request, "app_main/post_detail.html", context)


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'app_main/posts.html', {'posts': all_posts})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'app_main/new_post.html', {'form': form})