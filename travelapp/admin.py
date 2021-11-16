from django.contrib import admin
from .models import place
from .models import blogs

# Register your models here.
admin.site.register(place)
admin.site.register(blogs)
list_display=['name']
list_editable=['name']
