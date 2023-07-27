from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

email = 'email@test.com'
password = 'StrongPassword!'

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def login_check(request):
    email_input = request.POST.get('email_input')
    password_input = request.POST.get('password_input')

    # Verifica se as credenciais estão corretas
    credentials = {'email': email, 'password': password}
    # correct_credentials = [email, password]

    if email_input == email and password_input == password:
        return render(request, 'users/login_check/login_sucessfull.html', {'email': email, 'password': password})
    else:
        messages.warning(request, 'Wrong Email or Password. Try Again')
        return render(request, 'users/home.html')
        #return render(request, 'users/login_check/login_fail.html', {'email': email, 'password': password})
