from django.urls import path
from AppUser.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_request, name='UserLogin'),
    path('register/', register, name='UserRegister'),
    path('logout/', LogoutView.as_view(template_name='AppUser/logout.html'), name= 'UserLogOut')
]
