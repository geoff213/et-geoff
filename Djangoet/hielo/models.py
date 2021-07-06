from django.db import models

# Create your models here.
class Colaboradores(models.Model):
    Rut = models.CharField(primary_key=True, max_length=10, verbose_name='rut')
    Image = models.ImageField(upload_to='images/', null=True, blank = True)
    NombreCompleto = models.CharField(max_length=40, verbose_name='Nombre completo')
    Telefono = models.CharField(max_length=9, verbose_name='Numero de telefono')
    Direccion =  models.CharField(max_length=30, verbose_name='Direccion')
    Email = models.CharField(max_length=30, verbose_name='Email')
    Contrasenia = models.CharField(max_length=30, verbose_name='Contraseña')
    pais=models.CharField(max_length=10,verbose_name='pais')
    def __str__(self):
        return(self.nombreCompleto)