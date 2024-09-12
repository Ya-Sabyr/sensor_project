from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserCreateForm, LoginForm, UserUpdateForm
from .tasks import send_email_confirmation
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
            
            user = User.objects.create_user(
                username=user_username, email=user_email, password=user_password
            )
            user.is_active = False
            user.save()
            
            send_email_confirmation.delay(user.id)
            
            messages.success(request, "Регистрация успешна")
            
            return redirect(reverse('main:login'))
    else:
        form = UserCreateForm()
    return render(request, 'main/registration/registration.html', {'form': form})

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
    return render(request, 'main/registration/login.html', context)

@login_required(login_url='main:login')
def logout_user(request):
    session_key = list(request.session.keys())
    for key in session_key:
        if key == 'session_key':
            continue
        del request.session[key]
    logout(request)
    return redirect('main:main')

@login_required(login_url='main:login')
def profile_user(request):

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('main:account')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }
        
    return render(request, 'main/registration/account.html', context)

def main(request):
    return render(request, 'main/development/development.html')

def contacts(request):
    return render(request, 'main/development/development.html')

def about_us(request):
    return render(request, 'main/development/development.html')