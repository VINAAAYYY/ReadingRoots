from django.contrib import admin

# Register your models here.
from .models import book  # getting our product named class from models named file

admin.site.register(book)