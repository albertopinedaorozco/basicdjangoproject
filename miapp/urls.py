from django.urls import path
from .views import (cargar_inicio, LibroList, LibroCreate, 
LibroUpdate, LibroDelete, LibroDetalle,EjemplarList, 
PrestamoCreate, PrestamoList, LoginView, LogoutView)

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('libros/', LibroList.as_view(), name = 'listar_libros'),
    path('ejemplares/', EjemplarList.as_view(), name = 'listar_ejemplares'),
    path('libros/nuevo/', LibroCreate.as_view(), name = 'nuevo_libro'),
    path('libros/editar/<int:pk>', LibroUpdate.as_view(), name = 'editar_libro'),
    path('libros/eliminar/<int:pk>', LibroDelete.as_view(), name = 'borrar_libro'),
    path('libros/detalle/<int:pk>', LibroDetalle.as_view(), name = 'detalle_libro'),
    path('prestamo/nuevo/', PrestamoCreate.as_view(), name = 'nuevo_prestamo'),
    path('prestamos/', PrestamoList.as_view(), name = 'listar_prestamos'),
    path('iniciasesion/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logoutsesion/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    
]