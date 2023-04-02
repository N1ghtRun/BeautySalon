from django.urls import path
import admin_panel.views as views


urlpatterns = [
    path('', views.panel, name='panel'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_single),
    path('bookings/', views.bookings),
    path('specialist/', views.specialists, name='specialists'),
    path('specialist/<int:specialist_id>/', views.specialist_single),
    path('specialist/<int:specialist_id>/schedule/', views.specialist_schedule),
    path('specialist/<int:specialist_id>/schedule/<int:schedule_id>/', views.specialist_schedule_single),
]
