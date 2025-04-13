from django.shortcuts import render

# Create your views here.
"""
# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

"""
# users/views.py
from django.contrib.auth import login, get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import firebase_admin.auth

User = get_user_model()

@csrf_exempt
def firebase_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id_token = data.get("idToken")

        try:
            decoded_token = firebase_admin.auth.verify_id_token(id_token)
            email = decoded_token["email"]
            name = decoded_token.get("name", "")

            user, created = User.objects.get_or_create(email=email, defaults={"username": email.split("@")[0], "first_name": name})
            login(request, user)
            return JsonResponse({"success": True})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=401)

