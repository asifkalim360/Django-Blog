from django.urls import path
from blog import views
urlpatterns = [
    path('', views.home, name="home"), 
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('signup/', views.user_signup, name="signup"),
    path('login/', views.user_login, name="login"),
]
