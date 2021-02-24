from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_task/', views.add_task, name='add_task'),
    path('change_status/<int:task_id>/', views.change_status, name='change_status'),
    path('edit/<int:task_id>/', views.get_edit, name='edit'),
    path('edit_post/', views.post_edit, name='edit_post'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
]
