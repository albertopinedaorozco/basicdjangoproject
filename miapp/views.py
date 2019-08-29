from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Libro,Ejemplar,Prestamo

from .forms import PrestamoForm,DetallePrestamoFormSet

from django.http import HttpResponseRedirect

from django.contrib.auth.views import LoginView, LogoutView

def cargar_inicio(request):
    return render(request, "miapp/index.html")

class LibroList(ListView):
    model = Libro
    template_name = 'miapp/lista_libros.html'

class LibroDetalle(DetailView):
    model = Libro
    template_name = 'miapp/detalle_libro.html'

class LibroCreate(CreateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/nuevo_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroUpdate(UpdateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/actualizar_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'miapp/eliminar_libro.html'
    success_url = reverse_lazy('listar_libros')

#EJEMPLARES VIEWS
class EjemplarList(ListView):
    model = Ejemplar
    template_name = 'miapp/lista_ejemplares.html'

#prestamo views

class PrestamoList(ListView):
    model = Prestamo
    template_name = 'miapp/lista_prestamos.html'

class PrestamoCreate(CreateView):
    model = Prestamo
    form_class = PrestamoForm    
    template_name = 'miapp/nuevo_prestamo.html'
    success_url = reverse_lazy('listar_prestamos')

    #A partir de aqui vamos a usar dos metodos que son get y post, cada uno se ejecuta segun las peticiones que llegan del navegador
    #al servidor, si solo se requiere renderizar la pagina se va a ejecutar el metodo get (por ejemplo cuando en el form de listar prestamos damos click al boton Nuevo prestamo)
    #Cuando en ese mismo formulario se envian datos, esos datos se envian como POST y en ese caso se ejecuta el metodo post de esta vista que permita almacenar los datos del prestamo y su detalle

    # se ejecuta solo cuando se va a mostrar la pagina nuevo_prestamo.html sin enviar datos al servidor
    def get(self, request, *args, **kwargs):
            
        self.object = None
        #Instanciamos el formulario de PrestamoForm que declaramos en la variable form_class
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #Instanciamos el formset, el formset se llama DetallePrestamoFormSet y es un formulario personalizado para DetallePrestamo,
        #se encuentra en el archivo forms.py, el modelo Prestamo tambien tiene un formulario personalizado en el archivo forms.py
        detalle_orden_prestamo_formset=DetallePrestamoFormSet()
        
        #Renderizamos el formulario de prestamos y el formset 
        return self.render_to_response(self.get_context_data(form=form,
                                                            detalle_prestamo_form_set=detalle_orden_prestamo_formset))
    # se ejecuta solo cuando se da click en el boton enviar creando el prestamo (Se envian datos al servidor)
    def post(self, request, *args, **kwargs):
        
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #Obtenemos el formset pero ya con lo que se le pasa en el POST (Los datos del detalle)
        detalle_prestamo_form_set = DetallePrestamoFormSet(request.POST)
        
        #Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
        #form.valid() o en caso contrario se llama al método form_invalid()
        
        if form.is_valid() and detalle_prestamo_form_set.is_valid():
            return self.form_valid(form, detalle_prestamo_form_set)
        else:
            return self.form_invalid(form, detalle_prestamo_form_set)

    def form_valid(self, form, detalle_prestamo_form_set):

        #Aquí ya guardamos el object de acuerdo a los valores del formulario de prestamo
        self.object = form.save()
        #Utilizamos el atributo instance del formset para asignarle el valor del objeto Prestamo creado y que nos indica el modelo Foráneo
        detalle_prestamo_form_set.instance = self.object
        #Finalmente guardamos el formset para que tome los valores que tiene
        detalle_prestamo_form_set.save()
        #Redireccionamos a la ventana del listado de prestamos
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_prestamo_form_set):
        #Si es inválido el form de Prestamo o el formset renderizamos los errores
        return self.render_to_response(self.get_context_data(form=form,
                                                            detalle_prestamo_form_set = detalle_prestamo_form_set))


    
    

    



