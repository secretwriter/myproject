from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Student

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        enrollment_date = request.POST.get('enrollment_date')

        # Optional: Check if email is already used
        if Student.objects.filter(email=email).exists():
            return render(request, 'capstone_app/signup.html', {'error': 'Email already registered'})

        # Hash the password before saving
        hashed_password = make_password(password)

        # Save data to the database
        Student.objects.create(
            name=name,
            email=email,
            password=hashed_password,
            enrollment_date=enrollment_date
        )

        # Redirect to success page
        return redirect('success')

    return render(request, 'capstone_app/signup.html')


def success_page(request):
    return render(request, 'capstone_app/success.html')


def index(request):
    return render(request, 'capstone_app/index.html')


def chess_page(request):
    return render(request, 'capstone_app/chess.html')


def four_page(request):
    return render(request, 'capstone_app/four.html')


def kd_page(request):
    return render(request, 'capstone_app/kd.html')


def login_page(request):
    return render(request, 'capstone_app/login.html')


def ludo_page(request):
    return render(request, 'capstone_app/ludo.html')


def logintest_page(request):
    return render(request, 'capstone_app/logintest.html')


def more_page(request):
    return render(request, 'capstone_app/more.html')


def one_page(request):
    return render(request, 'capstone_app/one.html')


def options_page(request):
    return render(request, 'capstone_app/options.html')




def start_page(request):
    return render(request, 'capstone_app/start.html')


def three_page(request):
    return render(request, 'capstone_app/three.html')


def tic_tac_toe_page(request):
    return render(request, 'capstone_app/tic_tac_toe.html')


def two_page(request):
    return render(request, 'capstone_app/two.html')


def five_page(request):
    return render(request, 'capstone_app/five.html')
