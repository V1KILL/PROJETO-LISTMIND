from django.urls import path
from .views import ViewHome, ViewAddClient
urlpatterns = [
    path('', ViewHome, name="home"),
    path('addclient/<str:name>/<str:phonenumber>/<str:price>/<str:description>', ViewAddClient, name="addclient"),
]