from django.urls import path
import admin_panel.views as views


urlpatterns = [
    path('', views.panel),
    path('bookings/', views.bookings),
    path('specialist/', views.specialist),
    path('specialist/<int:specialist_id>/', views.specialist_single),
]