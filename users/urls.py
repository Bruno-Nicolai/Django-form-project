from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="authentication"),
    path('logout/', views.leave, name="logout"),
    path('main/', views.go_to_form, name="main"),
    path('send_email/', views.send_message, name="send_email"),
]