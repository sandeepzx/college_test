from django.urls import path
from . import views
app_name = 'schoolapp'
urlpatterns = [
    path('', views.home , name='home'),
    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
    path('register/', views.Register , name='register'),
    path('new/', views.new , name='new'),
    path('n/', views.n , name='n'),

]
