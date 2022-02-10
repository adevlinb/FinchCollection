from django.contrib import admin
from .models import Finch, Photo, Watching
# Register your models here.

admin.site.register(Finch)
admin.site.register(Watching)
admin.site.register(Photo)