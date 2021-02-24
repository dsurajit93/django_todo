from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('change_photo/', views.change_photo, name='change_photo'),
    path('logout/', views.logout, name='logout'),
]
