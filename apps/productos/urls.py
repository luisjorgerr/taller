from django.urls import path
from apps.productos.views import index,listado,categorias,viewProductos,agregarProducto,editarProducto,eliminarProducto,agregarCategoria

app_name='productos'
urlpatterns = [
    path('', index,name="index"),
    path('listado/',listado,name="lista"),
    path('categorias/',viewProductos.as_view(),name="categorias"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('editarProducto/<idProducto>',editarProducto,name="editarProducto"),	
    path('eliminarProducto/<idProducto>',eliminarProducto,name="eliminarProducto"),
    path('agregarCategoria/',agregarCategoria,name="agregarCategoria"),
    #path(' ',index), #esto sirve para poder entrar a una pagina sin tener que esxribir el complemento
    #path('plantilla/', plantilla),
    #path('especial',especial)
]
