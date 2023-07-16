from django.urls import path
from SorteoTique.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('inicio/', inicio, name ="Inicio"),
    path('draws/', draws, name="Draws"),
    path('clients/', clients, name="Clients"),
    path('sellers/', sellers, name="Sellers"),
    path('prizes/', prizes, name="Prizes"),
    path('tickets/', contactClient, name="Tickets"),

    path('contactClient/', contactClient, name="contactClient"),
    path('getSeller/', getSeller, name="getSeller"),
    path('buscarVendedor/', buscarVendedor, name="buscarVendedor"),
    path('deleteContactClient/<name_contactClient>', deleteContactClient, name="deleteContactClient"),
    path('editClient/<name_contactClient>', editClient, name="editClient"),
    path('editClient/<name_contactClient>', editClient, name="editClient"),
    
    path('Logout/',LogoutView.as_view(template_name = 'SorteoTique/login.html'), name="Logout"),
    path('login/', loginSellers, name="login"),
    path('register/', register, name="register"),

    path('profile/', profileView, name="profile"),
    path('Profile/editProfile/', editProfile, name="editProfile"),
    path('Profile/changePassword/', changePassword, name="changePassword"),
    path('Profile/changeAvatar/', changeAvatar, name="changeAvatar"),
    
]
