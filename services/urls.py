from django.urls import path
import services.views as views


urlpatterns = [
    path('', views.root, name='index'),
    path('services/', views.services, name='services'),
    path('services/<str:service_id>/', views.service_single),
    path('specialists/', views.specialists, name='specialists'),
    path('specialists/<int:specialist_id>/', views.specialist_single),
    path('booking/', views.booking, name='booking'),
]
