from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views


from .views import Index, MonedaView, MonedaNew, MonedaVer, \
    MonedaEdit, monedaEstado, monedaMaestra


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



] 