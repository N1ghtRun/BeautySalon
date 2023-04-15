from django.urls import path
import admin_panel.views as views


urlpatterns = [
    path('', views.panel, name='panel'),
    path('services/', views.services, name='admin_services'),
    path('services/<int:service_id>/', views.service_single),
    path('specialists/', views.specialists, name='admin_specialists'),
    path('specialist/<int:specialist_id>/', views.specialist_single),
    path('specialist/<int:specialist_id>/schedule/', views.specialist_schedule),
    path('specialist/<int:specialist_id>/schedule/<int:schedule_id>/', views.specialist_schedule_single),
]
