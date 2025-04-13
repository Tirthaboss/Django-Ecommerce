# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
"""
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
"""
	path("firebase-login/", firebase_login, name="firebase_login"),

]
