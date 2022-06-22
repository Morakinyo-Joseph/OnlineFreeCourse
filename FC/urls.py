
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teach/', include('teacher.urls', namespace="teach")),
    path('learn/', include('student.urls', namespace="learn")),
]
