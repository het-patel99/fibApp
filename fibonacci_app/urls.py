from django.urls import path
from . import views

urlpatterns = [
    path('', views.fibonacci_form, name='fibonacci_form'),
    path('result/<int:n>/<str:identifier>/', views.fibonacci_result, name='fibonacci_result'),
]