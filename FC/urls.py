
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teach/', include('teach.urls', namespace="teach")),
]
