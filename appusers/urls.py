from django.urls import path
from .views import ViewHome, ViewAddClient, ViewArchived, ViewServiceEdit, ViewClientDelete, ViewDashBoard, ViewDocument
urlpatterns = [
    path('', ViewHome, name="home"),
    path('addclient/<str:name>/<str:defeito>/<str:opcao>/<str:predictedDate>/<int:predictedPreco>/<int:preco>/<str:servico>/<str:peca>', ViewAddClient, name="addclient"),
    path('archived', ViewArchived,name='archived'),
    path('serviceedit/<str:status>/<int:id>/<str:name>/<str:description>', ViewServiceEdit,name='serviceedit'),
    path('clientdelete/<int:id>', ViewClientDelete, name="clientdelete"),
    path('dashboard', ViewDashBoard,name='dashboard'),
    path('document/<int:id>', ViewDocument,name='document'),

]