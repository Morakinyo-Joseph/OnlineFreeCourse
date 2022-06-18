
from django.urls import path
from . import views

app_name = "teacher"

urlpatterns = [
    path('', views.signup, name="signup"),
    path('view', views.display, name="display"),
]
