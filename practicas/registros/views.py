from django.shortcuts import render
from .forms import ComentarioContactoForm

from .models import Alumnos 

from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages 


# Create your views here.
def registros(request):
	alumnos=Alumnos.objects.all()
	return render(request, "registros/principal.html",{'alumnos':alumnos})

def contacto(request):
	return render(request,"registros/contacto.html")
	#Indicamos el lugar donde se renderizará el resultado de esta vista
	

def registrar(request):
	if request.method == 'POST':
		form = ComentarioContactoForm(request.POST)
		if form.is_valid(): #Si los datos recibidos son correctos
			form.save() #inserta
			return render(request,'registros/contacto.html') 
	form = ComentarioContactoForm()
	#Si algo sale mal se reenvian al formulario los datos ingresados
	return render(request,'registros/contacto.html',{'form': form}) 

# filter nos retornará los registros que coinciden con los parámetros de #búsqueda dados.
def consultar1(request, c):
#con una sola condición
	alumnos= Alumnos.objects.filter(carrera=c)
	return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consultar2(request):
	#multiples condiciones adicionando .filter() se analiza #como AND
	alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
	return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consultar3(request):
	#Si solo deseamos recuperar ciertos datos agregamos la #función only, listando los campos que queremos obtener de #la consulta emplear filter() o #en el ejemplo all()
	alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
	return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consultar4(request):
	alumnos=Alumnos.objects.filter(turno__contains="Vesp")
	return render(request,"registros/consultas.html",{'alumnos':alumnos})


def archivos(request):
	if request.method == 'POST':
		form = FormArchivos(request.POST, request.FILES)
		if form.is_valid():
			titulo = request.POST['titulo']
			descripcion = request.POST['descripcion']
			archivo = request.FILES['archivo']
			insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
			insert.save()
			return render(request,"registros/archivos.html")
		else:
			messages.error(request, "Error al procesar el formulario")
	else:
		return render(request,"registros/archivos.html",{'archivo':Archivos})

