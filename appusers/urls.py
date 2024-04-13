from django.urls import path
from .views import ViewHome, ViewAddClient, ViewArchived, ViewServiceEdit, ViewClientDelete, ViewDashBoard, ViewDocument, ViewGarantidos
urlpatterns = [
    path('', ViewHome, name="home"),
    path('addclient/<str:name>/<str:defect>/<str:option>/<str:predicted_date>/<int:predicted_price>/<int:price>/<str:service>/<str:part>', ViewAddClient, name="addclient"),
    path('archived', ViewArchived,name='archived'),
    path('serviceedit/<str:status>/<int:id>/<str:name>/<str:description>', ViewServiceEdit,name='serviceedit'),
    path('clientdelete/<int:id>', ViewClientDelete, name="clientdelete"),
    path('dashboard', ViewDashBoard,name='dashboard'),
    path('document/<int:id>', ViewDocument,name='document'),
    path('garantidos', ViewGarantidos, name='garantidos'),
]