from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *

###Boton Import Export en sitio de administracion de Django
class CategoriaResource(resources.ModelResource):

    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):

    class Meta:
        model = Autor

class PostResource(resources.ModelResource):

    class Meta:
        model = Post

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    #barra de busqueda del sitio de administracion de django para Categoria
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
    ###relacionado a boton Import Export en admin
    resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    #barra de busqueda del sitio de administracion de django para Autor
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
    ###relacionado a boton Import Export en admin
    resource_class = AutorResource

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    #barra de busqueda del sitio de administracion de django para Autor
    search_fields = ['titulo']
    list_display = ('titulo', 'estado', 'fecha_creacion')
    ###relacionado a boton Import Export en admin
    resource_class = PostResource

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)