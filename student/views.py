from django.shortcuts import render
from student.models import Student
from student.forms import StudentsignupForm
from django.shortcuts import render, redirect
from student.forms import StudentsignupForm
from student.models import Student
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, logout, login

User = get_user_model()

# Create your views here.
def Studentsignup(request):
    form = StudentsignupForm

    if request.method == 'POST':
        Username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            
            if User.objects.filter(username=Username).exists():
                messages.info(request, 'Username already exists!')
                return redirect("learn:signup")

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect("learn:signup")

            else:
                form = User.objects.create_user(username=Username, email=email, password=password)
                form.save()
                return redirect("learn:login")
        else:
            messages.info(request, 'Passwords do not match')
            return redirect("learn:signup")
    else:
        form = StudentsignupForm
    return render(request, 'student_register/studentsignup.html', {'form': form})

