from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import UserCreateForm, LoginForm
# Create your views here.
User = get_user_model()

def registration(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        
        if form.is_valid():
            form.save(commit=False)
            user_email = form.cleaned_data.get('email')
            user_username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            
            user = User.objects.create_user(username=user_username, email=user_email, password=user_password)
            user.is_active = False
            
            return redirect('/login/')
        else:
            form = UserCreateForm()
        return render(request, 'main/registration.html', {'form': form})

def login_user(request):
    
    form = LoginForm()
    
    if request.user.is_authenticated:
        return redirect('main:main')
    
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('main:main')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('main:login')
    context = {
        "form": form
    }
    return render(request, 'main/login.html', context)


def logout_user(request):
    session_key = list(request.session.keys())
    for key in session_key:
        if key == 'session_key':
            continue
        del request.session[key]
    logout(request)
    return redirect('main:main')


def main(request):
    return redirect('reports:reports')