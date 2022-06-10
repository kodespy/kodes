from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views


from .views import Index, MonedaView, MonedaNew, MonedaVer, \
    MonedaEdit, monedaEstado, monedaMaestra
from .views import MarcaView, MarcaNew, MarcaVer, \
    MarcaEdit, marcaEstado
from .views import CategoriaView, CategoriaNew, CategoriaVer, \
    CategoriaEdit, categoriaEstado
from .views import SubCategoriaView, SubCategoriaNew, SubCategoriaVer, \
    SubCategoriaEdit, subcategoriaEstado
from .views import ProveedorView, ProveedorNew, ProveedorVer, \
    ProveedorEdit, proveedorEstado
from .views import ProductoView, ProductoNew, ProductoVer, \
    ProductoEdit, productoEstado

from .views import ComprarView, ComprarNew, guardarCompras




urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), 
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
     next_page=reverse_lazy('mistock:login')), name='logout'),  
    path('monedas/', MonedaView.as_view(), name='moneda_list'),
    path('monedas/ver/<int:pk>', MonedaVer.as_view(), name='moneda_ver'),
    path('monedas/new', MonedaNew.as_view(), name='moneda_new'),
    path('monedas/edit/<int:pk>', MonedaEdit.as_view(), name='moneda_edit'),    
    path('monedas/estado/<int:pk>/<estado>', monedaEstado, name='monedaEstado'),    
    path('maestra/', monedaMaestra, name='monedaMaestra'),    
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/ver/<int:pk>', CategoriaVer.as_view(), name='categoria_ver'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),    
    path('categorias/estado/<int:pk>/<estado>', categoriaEstado, name='categoriaEstado'),    
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/ver/<int:pk>', SubCategoriaVer.as_view(), name='subcategoria_ver'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/estado/<int:pk>/<estado>', subcategoriaEstado, name='subcategoriaEstado'),
    path('marcas/', MarcaView.as_view(), name='marca_list'),
    path('marcas/ver/<int:pk>', MarcaVer.as_view(), name='marca_ver'),
    path('marcas/new', MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),    
    path('marcas/estado/<int:pk>/<estado>', marcaEstado, name='marcaEstado'),    
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/ver/<int:pk>', ProveedorVer.as_view(), name='proveedor_ver'),    
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),    
    path('proveedores/estado/<int:pk>/<estado>', proveedorEstado, name='proveedorEstado'),
    path('productos/', ProductoView.as_view(), name='producto_list'),
    path('productos/new', ProductoNew.as_view(), name='producto_new'),
    path('productos/ver/<int:pk>', ProductoVer.as_view(), name='producto_ver'),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),    
    path('productos/estado/<int:pk>/<estado>', productoEstado, name='productoEstado'),    
    path('comprar/', ComprarView.as_view(), name='comprar_list'),
    path('comprar/new', ComprarNew.as_view(), name='comprar_new'),
    
    path('comprar/guardar', guardarCompras, name='guardarCompras'),    


] 