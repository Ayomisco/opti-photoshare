from email.mime import image
from unicodedata import category
# from multiprocessing import context
# from unicodedata import category
from django.shortcuts import render, redirect
from .models import Category, Photo

# from django.shortcuts import 


# Create your views here.


def gallery(request):

    # Category filtering
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all().order_by('id')
    else:
        photos = Photo.objects.filter(category__name__contains =category )

    categories = Category.objects.all().order_by('-created_at')
    
    # photos = Photo.objects.all().order_by('id')
    context = {
        'categories': categories,
        'photos': photos
    }
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo': photo
    }
    return render(request, 'photos/photo.html', context)

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form_input = request.POST
        image = request.FILES.get('image')

        if form_input['category'] != 'none':
            category = Category.objects.get(id=form_input['category'])
        elif form_input['category_new'] != '':
            category, created = Category.objects.get_or_create(name=form_input['category_new'])
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