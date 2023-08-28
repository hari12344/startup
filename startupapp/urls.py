from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('home/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('courses/', courses, name='courses'),
    path('course/<str:id>/', course, name='course'),
    path('enroll/', enroll, name='enroll'),
    path('profile/', profile, name='profile'),
    path('profileupdate/<id>/', profileUpdate, name='profileupdate'),
    path('attendence/', attendence, name='attendence'),
    path('Request-reset-password/', RequestResetPassword.as_view(), name='reset-password'),
    
]