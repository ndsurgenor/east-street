from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('location/', views.location, name='location'),
    path('bookingsite/', views.BookFormView.as_view(), name='bookingsite'),
    path('bookinglist/', views.BookListView.as_view(), name='bookinglist'),
    path('<pk>/update/', views.BookUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.BookDeleteView.as_view(), name='delete'),
]
