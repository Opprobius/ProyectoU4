from django.urls import path
from .views import RegisterView, Login
from django.contrib.auth.views import  logout_then_login

urlpatterns=[
    path("registro/",RegisterView.as_view(),name="registro"),
    path('logout/', logout_then_login, name='logout'),
    path('accounts/login/',Login.as_view(), name='login'),
]