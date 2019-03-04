from django.contrib import admin
from .models import *

class Useradmin(admin.ModelAdmin):
    list_display = ('username',)

class Itemadmin(admin.ModelAdmin):
    list_display=('price',)

admin.site.register(User,Useradmin)
admin.site.register(Item,Itemadmin)
