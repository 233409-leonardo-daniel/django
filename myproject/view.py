from django.shortcuts import get_object_or_404
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from .models import Carrera
from .vistas import FormCarrera
from django.shortcuts import redirect



def index(request):
    return HttpResponse ("Hola mundo")

class HomePageView(TemplateView):
    template_name='home.html'
    model= Carrera
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saludo"]="hola de nuevo"
        context["lista"]=self.model.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name='about.html'

class CarreraCreateViewPage(TemplateView):
    template_name = "carreras_form.html"
    
    def get(self, request, *args, **kwargs):
        form = FormCarrera
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = FormCarrera(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return self.render_to_response({'form': form})
        
class CarreraEditarPageView(TemplateView):
    template_name= 'carreras_form.html'
    def get(self, request, pk, *args, **kwargs):
        carrera = get_object_or_404(Carrera, pk=pk)
        form = FormCarrera(instance=carrera)
        return self.render_to_response({'form': form})
    def post(self, request, pk, *args, **kwargs):
        carrera = get_object_or_404(Carrera, pk=pk)
        form = FormCarrera(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})
        

class CarreraEliminarPageView (TemplateView):
    template_name= 'carreras_form.html'
    def get(self, request, pk, *args, **kwargs):
        carrera = get_object_or_404(Carrera, pk=pk)
        form = FormCarrera(instance=carrera)
        carrera.delete()
        return redirect("/")