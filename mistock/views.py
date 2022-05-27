from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


from kodes.models import Usuario
from .models import Moneda
from .forms import MonedaForm




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
        return Moneda.objects.filter(uc_id=self.request.user.empresa.id).order_by('descripcion')


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
