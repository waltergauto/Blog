from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Post, Categoria

# Create your views here.
def home(request):

    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)

    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset)).distinct()

    #recibe dos parametros: la lista a mostrar y la cantidad de elementos a mostrar
    paginator = Paginator(posts, 3)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts': posts})

def generales(request):

    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Generales'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado = True, categoria = Categoria.objects.get(nombre_iexact = 'Generales'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, 'generales.html', {'posts': posts})

def redes(request):

    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Redes'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado = True, categoria = Categoria.objects.get(nombre_iexact = 'Redes'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, 'redes.html', {'posts': posts})

def videojuegos(request):

    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact = 'Videojuegos'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado = True, categoria = Categoria.objects.get(nombre_iexact = 'Videojuegos'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, 'videojuegos.html', {'posts': posts})

def programacion(request):

    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact = 'Programacion'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado = True, categoria = Categoria.objects.get(nombre_iexact = 'Programacion'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, 'programacion.html', {'posts': posts})

def detallePost(request, slug):

    post = get_object_or_404(Post, slug = slug) #si encuentra el objeto lo trae, si no retorna 404
    return render(request, 'post.html', {'detalle_post': post})