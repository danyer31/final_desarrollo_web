from . import views
from django.urls import include, path

urlpatterns = [
    #Cliente
    path('cliente/', views.ClienteListView.as_view(), name='cliente_list'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('cliente/add/', views.ClienteCreateView.as_view(), name='cliente_add'),
    path('cliente/<int:pk>/edit/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    
    #Venta    
    path('venta/', views.VentaListView.as_view(), name='venta_list'),
    path('venta/<int:pk>/', views.VentaDetailView.as_view(), name='venta_detail'),
    path('venta/add/', views.VentaCreateView.as_view(), name='venta_add'),
    path('venta/<int:pk>/edit/', views.VentaUpdateView.as_view(), name='venta_update'),
    path('venta/<int:pk>/delete/', views.VentaDeleteView.as_view(), name='venta_delete'),
]