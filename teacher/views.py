from django.shortcuts import render, redirect
# from .forms import TeacherCreationForm
# from .models import TeacherModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# def signup(request):
#     form = TeacherCreationForm(request.POST)
#     if form.is_valid():
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         firstname = form.cleaned_data['first_name']
#         last_name = form.cleaned_data['last_name']
#         email = form.cleaned_data['email']
#         dob = form.cleaned_data['date_of_birth']
#         gender = form.cleaned_data['gender']
#
#         if password1 == password2:
#             if TeacherModel.objects.filter(email=email).exists():
#                 messages.info(request, 'email already exits')
#                 return redirect('teach:signup')
#
#             else:
#                 new_teacher = TeacherModel.objects.create(first_name=firstname, last_name=last_name, email=email,
#                                                           password=password1, date_of_birth=dob, gender=gender)
#                 new_teacher.save()
#                 return redirect('teach:display')
#         else:
#             messages.info(request, 'password do not match!')
#             return redirect('teach:signup')
#
#     return render(request, "register/signup.html", {"form": form})
#
#
# def logging_in(request):
#     if request.method == "POST":
#         email = request.post['email']
#         password = request.post['password']
#
#         if TeacherModel.objects.filter(email=email).exists():
#             if TeacherModel.objects.filter(password=password).exists():
#                 user = authenticate(TeacherModel.objects.filter(email=email, password=password))
#                 login(request, user)
#                 return redirect('teach:display')
#
#     return render(request, "register/login.html")
#
#
# def home_display(request):
#     user = TeacherModel.objects.all()
#     return render(request, "teacher/display.html", {"user": user})
