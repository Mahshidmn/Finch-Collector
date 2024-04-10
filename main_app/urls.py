from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('finchs/', views.finchs_index, name="index"),
    path('finchs/<int:finch_id>', views.finchs_detail, name="detail"),
    path('finchs/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),   
    path('finchs/create/', views.FinchCreate.as_view(), name='finchs_create'),
    path('finchs/<int:pk>/update/', views.FinchUpdate.as_view(), name='finchs_update'),
    path('finchs/<int:pk>/delete/', views.FinchDelete.as_view(), name='finchs_delete'),
    path('finchs/<int:finch_id>/add_toy/<int:toy_id>/', views.add_toy, name='add_toy'), 
    path('finchs/<int:finch_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),   

    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]