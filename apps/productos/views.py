from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.productos.models import producto,categoria
from django.views.generic.list import ListView

from apps.productos.formulario import ProductoForm,CategoriaForm #importamos nuestros forms 


#from apps.categorias.models import categoria
#from django.http import HttpResponse
# Create your views here.
#def index(request): #genera la llamada a la pagina
#	return HttpResponse("Esta es la respuesta")#respuesat del servidor a la pagina

def index(request): #genera la llamada a la pagina
	return HttpResponse("Esta es la respuesta index")#respuesat del servidor a la pagina

def listado(request):
	contexto = { 
		'productos': producto.objects.all(),'categorias': categoria.objects.all()
	}
	
		
	
	return render(request, 'productos/listado.html',contexto)
	#return HttpResponse("Esta es la respuesta listado")

def categorias(request):
	contexto = { 
		'categorias': categoria.objects.all()
	}
	return render(request, 'productos/categorias.html',contexto)
	#return HttpResponse("Esta es la respuesta cate")

class viewProductos(ListView):
	
	model= producto
	queryset=producto.objects.filter(nombre="leche lala")
	template_name='productos/categorias.html'
		
def agregarProducto(request):
	if request.method == 'POST':
		form=ProductoForm(request.POST) #verificar si el formulario fue mandado el POST
		if form.is_valid(): #verifciar si el formulario en valido
			form.save() #guarda el formulario
		return redirect('productos:lista') #redireciona a otra pagina
	else: 
		form = ProductoForm() #crearemos objeto forms que importamos de nuestro form

	
	return render(request,'productos/formularioProducto.html')


def editarProducto(request,idProducto): 

	Producto=producto.objects.get(id=idProducto)#Sacamos la informacion del cliente de la base de datos
	idp=idProducto
	#return HttpResponse(Producto.nombre)
	#Cambiar la info de la base de datos

	if(request.method=='GET'):
		form=ProductoForm(instance=Producto) #creamos un formulario con los datos del cliente

	else:
		form=ProductoForm(request.POST,instance=Producto) #creamos un formulario con los datos del cliente
		if form.is_valid(): #verifciar si el formulario en valido
			form.save()
		return redirect('productos:lista')


	return render(request,'productos/editarProducto.html',{'form': form})

def eliminarProducto(request,idProducto):
	Producto=producto.objects.get(id=idProducto)
	Producto.delete()
	return redirect('productos:lista')


def agregarCategoria(request):
	if request.method == 'POST':
		form=CategoriaForm(request.POST) #verificar si el formulario fue mandado el POST
		if form.is_valid(): #verifciar si el formulario en valido
			form.save() #guarda el formulario
		return redirect('productos:lista') #redireciona a otra pagina
	else: 
		form = CategoriaForm() #crearemos objeto forms que importamos de nuestro form

	
	return render(request,'productos/formularioCategorias.html',{'form': form})