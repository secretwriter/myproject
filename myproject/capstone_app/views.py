from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Student, Game
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# ✅ SIGNUP FUNCTION


def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        enrollment_date = request.POST.get('enrollment_date')

        if User.objects.filter(username=email).exists():
            return render(request, 'capstone_app/signup.html', {'error': 'Email already registered'})

        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        Student.objects.create(user=user, enrollment_date=enrollment_date)

        return redirect('success')

    return render(request, 'capstone_app/signup.html')


# ✅ SUCCESS PAGE
def success_page(request):
    return render(request, 'capstone_app/success.html')


# ✅ GAME & STATIC PAGES
def index(request): return render(request, 'capstone_app/index.html')
def chess_page(request): return render(request, 'capstone_app/chess.html')
def four_page(request): return render(request, 'capstone_app/four.html')
def kd_page(request): return render(request, 'capstone_app/kd.html')
def login_page(request): return render(request, 'capstone_app/login.html')
def ludo_page(request): return render(request, 'capstone_app/ludo.html')
def logintest_page(request): return render(request, 'capstone_app/logintest.html')
def more_page(request): return render(request, 'capstone_app/more.html')
def one_page(request): return render(request, 'capstone_app/one.html')
def options_page(request): return render(request, 'capstone_app/options.html')
def start_page(request): return render(request, 'capstone_app/start.html')
def three_page(request): return render(request, 'capstone_app/three.html')
def tic_tac_toe_page(request): return render(request, 'capstone_app/tic_tac_toe.html')
def two_page(request): return render(request, 'capstone_app/two.html')
def five_page(request): return render(request, 'capstone_app/five.html')
def chatbox_page(request): return render (request, 'capstone_app/chatbox.html')

# ✅ DASHBOARD VIEW
@login_required(login_url='/admin-login/')
def admin_dashboard(request):
    return render(request, "admin_dashboard.html", {"user": request.user})


# ✅ API STATS
def total_users(request):
    return JsonResponse({'count': Student.objects.count()})

def total_games(request):
    return JsonResponse({'count': Game.objects.count()})

def pending_requests(request):
    return JsonResponse({'count': Game.objects.filter(status='pending').count()})


# ✅ FRONTEND LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect(request.GET.get("next", "index"))
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


# ✅ LOGOUT VIEW
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


# ✅ ADMIN LOGIN
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            try:
                student = Student.objects.get(user=user)
                if student.role == 'admin':
                    login(request, user)
                    return redirect('admin_dashboard')
                else:
                    return render(request, "admin_login.html", {"error": "Not an admin"})
            except Student.DoesNotExist:
                return render(request, "admin_login.html", {"error": "Student profile not found"})
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials"})

    return render(request, "admin_login.html")
