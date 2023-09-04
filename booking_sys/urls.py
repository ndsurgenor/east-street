from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('location/', views.location, name='location'),
    path('bookingsite/', views.BookingFormView.as_view(), name='bookingform'),
    path('userbookings/', views.UserBookings.as_view(), name='bookingsite'),
    path('<slug:slug>/', views.BookingDetail.as_view(), name='bookingdetail'),
]
