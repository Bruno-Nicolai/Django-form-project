from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.signin, name="authentication"),
    path('logout/', views.leave, name="logout"),
    # path('reset/', views.password_reset, name="reset"),
    path('main/', views.go_to_form, name="main"),
]