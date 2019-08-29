from django import forms
from .models import Prestamo,DetallePrestamo

from django.forms.models import inlineformset_factory

from django.forms import SelectDateWidget

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = ['fechaprestamo','nombre_cliente','telefono','estado']

    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class DetallePrestamoForm(forms.ModelForm):
        
    class Meta:
        model = DetallePrestamo
        fields = ['ejemplar','fechadedevolucion']

    def __init__(self, *args, **kwargs):
        super(DetallePrestamoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            

DetallePrestamoFormSet = inlineformset_factory(Prestamo, DetallePrestamo, form=DetallePrestamoForm, extra=3)