import uuid
import json
##
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
##
from django.http import HttpResponseRedirect
##

from kodes.models import Usuario
from .models import Moneda, Marca, Categoria, SubCategoria, Proveedor, Producto,\
    Compras
from .forms import MonedaForm, MarcaForm, CategoriaForm, SubCategoriaForm,\
    ProveedorForm, ProductoForm, ComprarForm


class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'    
    context_object_name = "obj"
    login_url = "mistock:login"

    def __init__(self):
        print("Index")
        

class MonedaView(LoginRequiredMixin, generic.ListView):
    model = Moneda
    template_name = "moneda_list.html"
    context_object_name = "obj"
    login_url = "mistock:login"

    def get_queryset(self):
        return Moneda.objects.order_by('descripcion').filter(uc_id=self.request.user.empresa.id)


class MonedaNew(LoginRequiredMixin, generic.CreateView):
    model = Moneda
    template_name = "moneda_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = MonedaForm
    success_url = reverse_lazy("mistock:moneda_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MonedaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Moneda
    template_name = "moneda_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = MonedaForm
    success_url = reverse_lazy("mistock:moneda_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class MonedaVer(LoginRequiredMixin, generic.UpdateView):
    model = Moneda
    template_name = "moneda_ver.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = MonedaForm
    success_url = reverse_lazy("mistock:moneda_list")


def monedaEstado(request, pk, estado):
    login_url = "mistock:login"
    moneda = Moneda.objects.filter(id=pk).first()
    contexto={}
    template_name="moneda_estado.html"
    if not moneda:
        return redirect("mistock:moneda_list")

    if request.method == 'GET':
        contexto={'obj': moneda}

    if request.method == 'POST':
        moneda.estado = estado
        moneda.save()
        contexto ={'obj': 'ok'}
        return redirect("mistock:moneda_list")

    return render(request, template_name, contexto) 


def monedaMaestra(self):
    login_url = "mistock:login"
    obj =  Moneda.objects.filter(maestra=True).first()
    id_maestra = 0
    if obj:
        id_maestra = obj.id
    return JsonResponse({'idmaestra':id_maestra})

class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "marca_list.html"
    context_object_name = "obj"
    login_url = "mistock:login"

    def get_queryset(self):
        return Marca.objects.order_by('descripcion').filter(uc_id=self.request.user.empresa.id)


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = "marca_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = MarcaForm
    success_url = reverse_lazy("mistock:marca_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "marca_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = MarcaForm
    success_url = reverse_lazy("mistock:marca_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class MarcaVer(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "marca_ver.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = MarcaForm
    success_url = reverse_lazy("mistock:marca_list")


def marcaEstado(request, pk, estado):
    login_url = "mistock:login"
    marca = Marca.objects.filter(id=pk).first()
    contexto={}
    template_name="marca_estado.html"
    if not marca:
        #return HttpResponse('No existe' + str(pk))
        return redirect("mistock:marca_list")

    if request.method == 'GET':
        contexto={'obj': marca}

    if request.method == 'POST':
        marca.estado = estado
        marca.save()
        contexto ={'obj': 'ok'}
        #return HttpResponse('Estado cambiado a' + str(pk))
        return redirect("mistock:marca_list")

    return render(request, template_name, contexto) 

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "categoria_list.html"
    context_object_name = "obj"
    login_url = "mistock:login"

    def get_queryset(self):
        return Categoria.objects.order_by('descripcion').filter(uc_id=self.request.user.empresa.id)


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "categoria_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = CategoriaForm
    success_url = reverse_lazy("mistock:categoria_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "categoria_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = CategoriaForm
    success_url = reverse_lazy("mistock:categoria_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaVer(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "categoria_ver.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = CategoriaForm
    success_url = reverse_lazy("mistock:categoria_list")



class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "catalogo_estado.html"
    context_object_name = "obj"
    success_url = reverse_lazy("mistock:categoria_list")

def categoriaEstado(request, pk, estado):
    login_url = "mistock:login"
    categoria = Categoria.objects.filter(id=pk).first()
    contexto={}
    template_name="categoria_estado.html"
    if not categoria:
        return redirect("mistock:categoria_list")

    if request.method == 'GET':
        contexto={'obj': categoria}

    if request.method == 'POST':
        categoria.estado = estado
        categoria.save()
        contexto ={'obj': 'ok'}
        return redirect("mistock:categoria_list")

    return render(request, template_name, contexto) 
        


class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "subcategoria_list.html"
    context_object_name = "obj"
    login_url = "mistock:login"

    def get_queryset(self):
        return SubCategoria.objects.order_by('descripcion').filter(uc_id=self.request.user.empresa.id)

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = "subcategoria_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("mistock:subcategoria_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = "subcategoria_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("mistock:subcategoria_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)     

class SubCategoriaVer(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = "subcategoria_ver.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("mistock:subcategoria_list")



def subcategoriaEstado(request, pk, estado):
    login_url = "mistock:login"
    subcategoria = SubCategoria.objects.filter(id=pk).first()
    contexto={}
    template_name="subcategoria_estado.html"
    if not subcategoria:
        return redirect("mistock:subcategoria_list")

    if request.method == 'GET':
        contexto={'obj': subcategoria}

    if request.method == 'POST':
        subcategoria.estado = estado
        subcategoria.save()
        contexto ={'obj': 'ok'}
        return redirect("mistock:subcategoria_list")

    return render(request, template_name, contexto) 
        

class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = "proveedor_list.html"
    context_object_name = "obj"
    login_url = "mistock:login"

    def get_queryset(self):
        return Proveedor.objects.order_by('razonsocial').filter(uc_id=self.request.user.empresa.id)

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = "proveedor_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = ProveedorForm
    success_url = reverse_lazy("mistock:proveedor_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = "proveedor_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = ProveedorForm
    success_url = reverse_lazy("mistock:proveedor_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ProveedorVer(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = "proveedor_ver.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = ProveedorForm
    success_url = reverse_lazy("mistock:proveedor_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def proveedorEstado(request, pk, estado):
    login_url = "mistock:login"
    proveedor = Proveedor.objects.filter(id=pk).first()
    contexto={}
    template_name="proveedor_estado.html"
    if not proveedor:
        return redirect("mistock:proveedor_list")

    if request.method == 'GET':
        contexto={'obj': proveedor}

    if request.method == 'POST':
        proveedor.estado = estado
        proveedor.save()
        contexto ={'obj': 'ok'}
        return redirect("mistock:proveedor_list")

    return render(request, template_name, contexto) 

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "producto_list.html"
    context_object_name = "obj"
    login_url = "mistock:login"        

    def get_queryset(self):
        return Producto.objects.order_by('descripcion').filter(uc_id=self.request.user.empresa.id)


class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "producto_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = ProductoForm
    success_url = reverse_lazy("mistock:producto_list")


    def get_form_kwargs(self):
        kwargs = super(ProductoNew, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['existencia'] = 0
        return kwargs



    def form_valid(self, form):
        form.instance.uc = self.request.user
        form.instance.existencia_actual = form.instance.existencia_inicial
        return super().form_valid(form) 

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "producto_form.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = ProductoForm
    success_url = reverse_lazy("mistock:producto_list")

    def get_form_kwargs(self):
        kwargs = super(ProductoEdit, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['existencia'] = self.object.existencia_inicial
        return kwargs


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)             


class ProductoVer(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "producto_ver.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = ProductoForm
    success_url = reverse_lazy("mistock:producto_list")

def productoEstado(request, pk, estado):
    login_url = "mistock:login"
    producto = Producto.objects.filter(id=pk).first()
    contexto={}
    template_name="producto_estado.html"
    if not producto:
        return redirect("mistock:producto_list")

    if request.method == 'GET':
        contexto={'obj': producto}

    if request.method == 'POST':
        producto.estado = estado
        producto.save()
        contexto ={'obj': 'ok'}
        return redirect("mistock:producto_list")

    return render(request, template_name, contexto)         



class ComprarView(LoginRequiredMixin, generic.ListView):
    model = Compras
    template_name = "comprar_list.html"
    context_object_name = "obj"
    login_url = "mistock:login"  


class ComprarNew(LoginRequiredMixin, generic.CreateView):
    model = Compras
    template_name = "comprar_new.html"
    context_object_name = "obj"
    login_url = "mistock:login"
    form_class = ComprarForm
    success_url = reverse_lazy("mistock:comprar_list")

    def get_form_kwargs(self):
        kwargs = super(ComprarNew, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    def post(self, request):

        #kwargs['user'] = self.request.user
        #form = self.form_class(request.POST)
        print("-------------------------------------")
        print(request)
        print(self.request)
        print("-------------------------------------")
        print(self.request.POST['factura_fecha'])
        print(self.request.POST['factura_numero'])
        print(self.request.POST['proveedor'])
        print(self.request.POST['moneda'])
        print(self.request.POST['factura_tipo'])
        print(self.request.POST)

        #print(self.request.POST.factura_numero)
        return HttpResponseRedirect('/mistock/comprar')
        #if form.is_valid():
        #    print("Return.....")
        #    return HttpResponseRedirect('/comprar/')
        #print("Return.....0")    
        #return render(request, self.template_name, {'form': form})
        


    def form_valid(self, form):
        print("Validando.....")
        form.instance.uc = self.request.user
        return super().form_valid(form)    

def guardarCompras(request):
    login_url = "mistock:login"
    contexto = {}
    template_name = "comprar_new.html"
    context_object_name = "obj"
    form_class = ComprarForm
    detalle = request.POST.getlist('detalle[]')
    for x in detalle:
        i = x.split(',')
        print(i[0])    
        print(i[1])    
    if request.method == 'POST':
        print("Post - request.....")
        #producto.estado = estado
        #producto.save()
        #contexto ={'obj': 'ok'}
        return redirect("mistock:comprar_list")

    return render(request, template_name, contexto)         