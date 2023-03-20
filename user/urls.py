from django.urls import path
import user.views as views


urlpatterns = [
    path('', views.user),
    path('booking/', views.booking),
]