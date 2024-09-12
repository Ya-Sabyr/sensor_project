from django.urls import path
from .views import registration, login_user, logout_user, main, contacts, about_us, profile_user

app_name='main'

urlpatterns = [
    path('', main, name='main'),
    
    path('contacts/', contacts, name='contacts'),
    path('about-us', about_us, name='about-us'),
    path('account', profile_user, name='account'),
    #Reg/log
    path('registration/', registration, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
