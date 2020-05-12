from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('<int:t_id>/', views.delete, name='delete')


]