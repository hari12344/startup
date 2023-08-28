from django.urls import path
from .views import *
from .views import *

urlpatterns = [
    path('signup/',signup, name="signup"),
    path('login/',handleLogin, name="handellogin"),
    path('logout/',handleLogout, name="handlelogout"),
   
]