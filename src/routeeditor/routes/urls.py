from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_route, name='create_route'),
    path('', views.route_list, name='route_list'),
    path('<int:route_id>/edit/', views.edit_route, name='edit_route'),
]