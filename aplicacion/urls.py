from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home" ),
    path('profesores/', profesores, name="profesores" ),
    path('estudiantes/', estudiantes, name="estudiantes" ),
    path('entregables/', entregables, name="entregables" ),

    path('crear_profesor/', crear_profesor, name="crear_profesor" ),
    path('eliminar_profesor/<id_profesor>/', eliminar_profesor, name="eliminar_profesor" ),
    path('modificar_profesor/<id_profesor>/', modificar_profesor, name="modificar_profesor" ),

    path('cursos/', CursoList.as_view(), name="cursos" ),
    path('create_curso/', CursoCreate.as_view(), name="create_curso" ),
    path('update_curso/<int:pk>/', CursoUpdate.as_view(), name="update_curso" ),
    path('delete_curso/<int:pk>/', CursoDelete.as_view(), name="delete_curso" ),
]