from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('reciepts/<int:post_id>', views.detail, name='detail'),
    path('reciepts/year/<int:year>', views.reciepts_year, name="reciepts_year"),
    path('reciepts/year/<int:year>/month/<int:month>', views.reciepts_month, name="reciepts_month"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register")
]