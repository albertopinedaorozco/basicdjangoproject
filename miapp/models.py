from django.db import models

class Libro(models.Model):
    nombre = models.CharField("Nombre:",max_length=45)
    descripcion = models.TextField(max_length=45)
    isbn = models.CharField(max_length=45)
    copias = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    fechaprestamo = models.DateField("Fecha de prestamo")
    nombre_cliente = models.CharField(max_length=40)
    telefono = models.CharField(max_length=45)
    estado = models.BooleanField()

    def __str__(self):
        return "{0}-{1}".format(self.fechaprestamo, self.nombre_cliente)

class Ejemplar(models.Model):
    numeroejemplar = models.CharField(max_length=40)
    fechadecompra = models.DateField("Fecha de compra")
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE)

    def __str__(self):
        return self.numeroejemplar

class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey('Prestamo', on_delete=models.CASCADE)
    ejemplar = models.ForeignKey('Ejemplar', on_delete=models.CASCADE)




    
