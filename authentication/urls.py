from django.contrib import admin
from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    
]