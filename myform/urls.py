from django.urls import path, include
from . import views


urlpatterns = [
	path('contact/', views.contact, name='contact'),
	path('snippet/', views.snippet, name='snippet'),
   
   
]
