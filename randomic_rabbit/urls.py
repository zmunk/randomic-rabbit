from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('randomnumbers.urls')), # added
    path('admin/', admin.site.urls),
]
