from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.UserBookings.as_view(), name='bookings')
]