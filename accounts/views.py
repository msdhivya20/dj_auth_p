from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Registration Successful. Please login."
        )

        return redirect('login')

    return render(request, 'accounts/signup.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(
                request,
                "Please enter username and password."
            )
            return redirect('login')

        if not User.objects.filter(username=username).exists():
            messages.error(
                request,
                "Username is not registered."
            )
            return redirect('login')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is None:
            messages.error(
                request,
                "Incorrect password."
            )
            return redirect('login')

        login(request, user)

        messages.success(
            request,
            "Login successful."
        )

        return redirect('home')

    return render(request, 'accounts/login.html')


def logout_view(request):

    logout(request)

    return redirect('landing')


def forgot_username(request):

    if request.method == "POST":

        email = request.POST.get("email")

        try:

            user = User.objects.get(email=email)

            send_mail(
                subject="Username Recovery",
                message=f"Hello,\n\nYour username is: {user.username}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(
                request,
                "Username has been sent to your email."
            )

        except User.DoesNotExist:

            messages.error(
                request,
                "No account found with this email."
            )

    return render(
        request,
        "accounts/forgot_username.html"
    )