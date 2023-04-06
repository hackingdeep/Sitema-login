from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('bienvenido/',views.Bienvenido,name='bienvenido'),
    path('login/',views.IniciaSession,name='login'),
    path('register/',views.Register,name='register'),
    path('logout/',views.logou,name='logout'),
     path('delete_User/<int:id>',views.deleteUser,name='deleteUser'),

]