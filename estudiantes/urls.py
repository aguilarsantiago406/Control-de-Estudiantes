from django.urls import path
from . import views


app_name = "estudiantes"


urlpatterns = [
path('', views.lista, name='lista'),
path('nuevo/', views.crear, name='crear'),
path('<int:pk>/', views.detalle, name='detalle'),
path('<int:pk>/editar/', views.editar, name='editar'),
path('<int:pk>/eliminar/', views.eliminar, name='eliminar'),
]