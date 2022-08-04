from first_app import views
from django.urls import path

urlpatterns = [
	path('', views.home), 
	path('registrarCurso/', views.registrarCurso),
	path('eliminarCurso/<codigo>', views.eliminarCurso)
]
