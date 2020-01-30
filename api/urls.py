from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloAPI),
    path('person/', views.PersonAPI),
    path('email/', views.EmailAPI),
    path('auth/index/', views.UserIndexSerializer),
    path('auth/register/', views.RegistrationAPI.as_view()),
    path('auth/login/', views.LoginAPI.as_view()),
    path('auth/user/', views.UserAPI.as_view()),
    path('auth/profile/<int:user_pk>/update/', views.ProfileUpdateAPI.as_view()),
]
