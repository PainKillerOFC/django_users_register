from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'users/home.html')

def users(request):
    new_user = User()
    new_user.email = request.POST.get('email')
    new_user.password = request.POST.get('password')
    new_user.save()
    # exibir usurários cadastrados em uma nova página
    users = {
        'users': User.objects.all()
    }
    return render(request, 'users/user_list.html', users)