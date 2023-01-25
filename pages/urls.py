from django.urls import path

from .views import AboutusView, ContactusView, UserListView, HomeView, FirstPageView

urlpatterns = [
    path('', FirstPageView.as_view(), name='first_page'),
    path('home/', HomeView.as_view(), name='home'),
    path('aboutus/', AboutusView.as_view(), name='aboutus'),
    path('contactus/', ContactusView.as_view(), name='contactus'),
    path('userlist/', UserListView.as_view(), name='userlist')
    ]