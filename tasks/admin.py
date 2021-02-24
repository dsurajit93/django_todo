from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task', 'date', 'time', 'is_completed')
    list_display_links = ('id', 'task')
    list_editable = ('is_completed', )
    list_per_page = 25

admin.site.register(Task, TaskAdmin)
