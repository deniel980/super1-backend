from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import *


class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Users.objects.all()

        username = self.request.query_params.get("username")
        if username:
            queryset = queryset.filter(username=username)
            return queryset
    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]


class FavouriteCountryListCreateView(generics.ListCreateAPIView):
    serializer_class = FavouriteCountrySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = FavouriteCountry.objects.all()

        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)

        country = self.request.query_params.get('country_id')
        if country:
            queryset = queryset.filter(country_id=country)

        return queryset

    
    


class FavouriteCountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavouriteCountry.objects.all()
    serializer_class = FavouriteCountrySerializer
    permission_classes = [AllowAny]
