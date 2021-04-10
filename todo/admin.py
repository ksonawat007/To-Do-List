from django.contrib import admin
from .models import todolist

# Register your models here.
@admin.register(todolist)

class todolist(admin.ModelAdmin):
    list_display = ["content"]