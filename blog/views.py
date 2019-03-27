from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.contrib.auth import authenticate, login as _login, logout as _logout, get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
import datetime

from .models import Post, Comment
from .forms import RegisterForm, LoginForm, CommentForm



def index(request):
    last_reciepts = get_list_or_404(Post.objects.get_last_reciepts())

    context = {'first_row_reciepts': last_reciepts[:4],
               'second_row_reciepts': last_reciepts[4:8],
               'third_row_reciepts': last_reciepts[8:]
               }

    return render(request, "blog/last_posts.html", context)

def detail(request, post_id=1):

    post = get_object_or_404(Post.objects.get_reciept_by_id(post_id))
    comments = post.get_comments()


    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():

            Comment().add(post, request.user, request.POST['comment'], timezone.now())

            form = CommentForm() # return empty form to clean it's fields after submit

    else:
        if request.user.is_authenticated:
            form = CommentForm()
        else:
            form = None

    return render(request, 'blog/food-single.html', {'post': post, 'comments': comments, 'form': form})



def reciepts_year(request, year=timezone.now().year):

    reciepts = get_list_or_404(Post.objects.get_reciepts_year(year))
    months = {}

    for rec in reciepts:
        month_str = rec.modified_date.strftime("%B")
        month_num = rec.modified_date.strftime("%m")
        months.update({month_str: month_num})

    return render(request, 'blog/food-index.html', {'year': year, 'months': months})


def reciepts_month(request, year=timezone.now().year, month=timezone.now().month):

    reciepts = get_list_or_404(Post.objects.get_reciepts_month(year, month))

    return render(request, 'blog/food-index.html', {"month_reciepts": reciepts})



def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        print("username", username, password, user)

        if user is not None:
            if user.is_active:
                _login(request, user)
                return HttpResponseRedirect('/')
            else:
                pass

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            form = LoginForm()

    return render(request, 'blog/login_form.html', {'login_form': form})



def logout(request):
    if request.user.is_authenticated:
        _logout(request)
        return HttpResponseRedirect("/")
    else:
        pass

    return HttpResponseRedirect("/")




def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            # if request.POST["password"] != request.POST["password2"]:
            #
            #     return render(request, 'blog/food-index.html', {'register_form': form})

            print("username", request.POST["username"])
            User = get_user_model() # because you changed your user model see AUTH_USER_MODEL in settings.py

            user = User.objects.create_user(request.POST["username"],
                                           request.POST["email"],
                                           request.POST["password"])

            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]

            user.save()

            _login(request, user)

            return HttpResponseRedirect('/')

    else:
        form = RegisterForm()

    return render(request, 'blog/register_form.html', {'register_form': form})