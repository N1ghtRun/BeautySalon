from django.urls import path
import services.views as views


urlpatterns = [
    path('', views.root, name='index'),
    path('services/<str:service_name>/', views.service_single),
    path('specialist/', views.specialist),
    path('specialist/<int:specialist_id>/', views.specialist_single),
    path('booking/', views.booking, name='booking'),
]
