from django.contrib import admin

# Register your models here.
from .models import Songs,Artists

admin.site.register(Songs)
admin.site.register(Artists)
