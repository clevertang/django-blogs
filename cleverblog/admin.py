from django.contrib import admin

from cleverblog.models import Catagory, Blog, Tag
from . import  models
# Register your models here.
admin.site.register(Catagory)
admin.site.register(Blog)
admin.site.register(Tag)