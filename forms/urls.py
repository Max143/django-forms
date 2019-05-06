from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('form/', include('myform.urls')),
    path('admin/', admin.site.urls),
]
