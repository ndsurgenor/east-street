from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('location/', views.location, name='location'),
    path('bookingsite/', views.BookFormView.as_view(), name='bookingsite'),
    path('userbookings/', views.BookListView.as_view(), name='userbookings'),
    path('<pk>/delete/', views.BookDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.BookDetail.as_view(), name='detail'),
]
