from django.urls import path
from .views import ViewHome, ViewAddClient, ViewArchived, ViewEditClient, ViewDeleteClient, ViewDashBoard, ViewDocument, ViewGarantidos, ViewLogout, ViewSignin, ViewSignUp, ViewRecruiter
urlpatterns = [
    path('', ViewHome, name="home"),
    path('recruiter', ViewRecruiter, name="recruiter"),
    path('signup', ViewSignUp, name='signup'),
    path('signin', ViewSignin, name='signin'),
    path('logout', ViewLogout, name='logout'),
    path('addclient/<str:name>/<str:defect>/<str:option>/<str:predicted_date>/<int:predicted_price>/<int:price>/<str:service>/<str:part>', ViewAddClient, name="addclient"),
    path('editclient/<str:status>/<int:id>/<str:name>/<str:description>', ViewEditClient,name='editclient'),
    path('deleteclient/<int:id>', ViewDeleteClient, name="deleteclient"),
    path('archived', ViewArchived,name='archived'),
    path('garantidos', ViewGarantidos, name='garantidos'),
    path('dashboard', ViewDashBoard,name='dashboard'),
    path('document/<int:id>', ViewDocument,name='document'),
]