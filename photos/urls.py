from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Signup, name='register'),
    path('login/', LoginUser, name='login'),
path('logout/', LogoutUser, name='logout'),
    path('', gallery, name='gallery'),
    path('photo/<str:pk>/', viewPhoto, name='photo'),
    path('add/', addPhoto, name='add'),

]