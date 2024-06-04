from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserListCreateView.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('favouritecountry/', FavouriteCountryListCreateView.as_view(), name='favouritecountry-list-create'),
    path('favouritecountry/<int:pk>/', FavouriteCountryDetailView.as_view(), name='favouritecountry-detail'),
]
