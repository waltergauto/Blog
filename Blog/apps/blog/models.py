from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):

    id = models.AutoField('Identificador', primary_key = True)
    nombre= models.CharField('Nombre de la Categoria', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Estado', default = True)
    #auto_now se modifica cada vez que se actualiza el modelo, auto_now_add solo se agrega al crear el modelo
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):

    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Autor', max_length=255, null =False, blank=False)
    apellido = models.CharField('Apellido del Autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null = True, blank= True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    email = models.URLField('correo Electronico', null=False, blank=False)
    web = models.URLField('Pagina Web', null=True, blank=True)
    estado = models.BooleanField('Estado del Autor', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.nombre, self.apellido)

class Post(models.Model):

    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo del Post', max_length=100, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripcion', max_length=255, null=False, blank=False)
    contenido = RichTextField('Contenido', default=None)
    image = models.URLField('Imagen', max_length=255, blank=False, null=False)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
