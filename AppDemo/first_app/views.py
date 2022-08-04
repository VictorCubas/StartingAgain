from os import curdir
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

def home(request):
	#return HttpResponse('<h1>Hello world!</h1>')
	cursosListado = Curso.objects.all()
	return render(request, 'gestionCurso.html', {'cursos':cursosListado})

def registrarCurso(request):
	codigo = request.POST['txtCodigo']
	nombre = request.POST['txtNombre']
	creditos = request.POST['numCreditos']

	curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
	return redirect('/')

def eliminarCurso(request, codigo):
	curso = Curso.objects.get(codigo=codigo)
	curso.delete()
	return redirect('/')