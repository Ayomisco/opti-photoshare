from email.mime import image
from unicodedata import category
from django.http import HttpResponse
# from multiprocessing import context
# from unicodedata import category
from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Django forms
from photos.forms import SignupForm
# Create your views here.

def Signup(request):
    page = 'register'
    if request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect('index')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username=username, email=email, password=password)
            # messages.success(request, f"Account Created Successfully, {request.user.username}! ")
            return redirect('login')

    else:
        form = SignupForm()


    context = {
        'page': page,
        'form': form
    }
    return render(request, 'photos/login_register.html', context)

# def registerUser(request):
#     page = 'register'

#     form = CustomUserCreationForm()
#     context = {
#         'page': page,
#         'form': form
#     }
#     return render(request, 'photos/login_register.html', context)


def LoginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect ('gallery')

    context = {
       'page': page
    }
    return render(request, 'photos/login_register.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def gallery(request):

    if not request.user.is_authenticated:
        return redirect('login')
    else:

        user = request.user
        # Category filtering
        category = request.GET.get('category')
        if category == None:
            photos = Photo.objects.filter(category__user = user).order_by('-created_at')
        else:
            photos = Photo.objects.filter(category__name__contains =category, category__user = user )

        categories = Category.objects.filter(user=request.user) 
        
    # photos = Photo.objects.all().order_by('id')
    context = {
        'categories': categories,
        'photos': photos
    }
    return render(request, 'photos/gallery.html', context)

@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo': photo
    }
    return render(request, 'photos/photo.html', context)

@login_required(login_url='login')
def addPhoto(request):
    user = request.user
    categories = user.category_set.all()

    if request.method == 'POST':
        form_input = request.POST
        image = request.FILES.get('image')

        if form_input['category'] != 'none':
            category = Category.objects.get(id=form_input['category'])
        elif form_input['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=form_input['category_new'])
        else: 
            category = None

        photo = Photo.objects.create(
            category = category,

            description = form_input['description'],
            image = image

        )

        return redirect('gallery')

    context = {
        'categories': categories,
    }
    return render(request, 'photos/add-photo.html', context)