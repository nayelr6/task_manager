from django.contrib import admin

# Register your models here.


from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_displaay =['title','description','due_date','priority','complete','created_at','updated_at']
    list_filter = ['priority','complete']
    search_fields = ['title']
    ordering = ['priority']
    