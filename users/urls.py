from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.signin, name="authentication"),
    path('logout/', views.leave, name="logout"),
    path('main/', views.go_to_form, name="main"),
]