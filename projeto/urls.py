from django.contrib import admin
from django.urls import path
from app_home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('users/user_list', views.users, name = 'user_list')
]
