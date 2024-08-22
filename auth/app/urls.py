from django.urls import path,include
from .import views

urlpatterns = [

path('login',views.loginpage,name='loginpage'),
path('',views.signuppage,name='signuppage'),
path('user_create',views.user_create,name='user_create'),
path('log',views.log,name='log'),
path('adminmod',views.adminmod,name='adminmod'),
path('usermod',views.usermod,name='usermod'),
path('lgout',views.lgout,name='lgout'),

    
]
