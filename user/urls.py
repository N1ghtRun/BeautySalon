from django.urls import path
import user.views as views


urlpatterns = [
    path('', views.user_page),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]