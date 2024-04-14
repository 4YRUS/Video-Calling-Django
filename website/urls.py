
from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),
    path('room/',views.room,name='room'),
    path('joinroom/',views.joinroom,name='joinroom'),

]
