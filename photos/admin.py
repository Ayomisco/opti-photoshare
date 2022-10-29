from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register((Category, Photo))

admin.site.site_header = "Optimum Admin"
admin.site.site_title = "Optimum Media Admin Portal"
admin.site.index_title = "Welcome to Optimum Admin Website"