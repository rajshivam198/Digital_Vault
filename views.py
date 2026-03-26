from django.shortcuts import render, redirect
from django.contrib import messages

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == USERNAME and password == PASSWORD:
            request.session['user'] = username
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, "login.html")


def dashboard(request):
    if request.session.get('user'):
        return render(request, "dashboard.html", {'user': request.session['user']})
    return redirect('login')


def logout_view(request):
    request.session.flush()
    return redirect('login')