from django.shortcuts import render, HttpResponse


def principal(request):
	return render(request, "inicio/principal.html")

def contacto(request):
	return render(request, "inicio/contacto.html")

def formulario(request):
	return render(request, "inicio/formulario.html")

def ejemplo(request):
	return render(request,"inicio/ejemplo.html")

def seguridad(request, nombre=None, edad=None):
	nombre = request.GET.get('nombre')
	edad = request.GET.get('edad')
	return render(request,"inicio/seguridad.html",
	{'nombre':nombre,'edad':edad})


def editarComentarioContacto(request, id):
	comentario = get_object_or_404(ComentarioContacto, id=id)
	form = ComentarioContactoForm(request.POST, instance=comentario)
	#Referenciamos que el elemento del formulario pertenece al comentario 
	# ya existente
	if form.is_valid():
		form.save() #si el registro ya existe, se modifica. 
		comentarios=ComentarioContacto.objects.all()
		return render(request,"registros/consultaContacto.html",
			{'comentarios':comentarios})
	#Si el formulario no es valido nos regresa al formulario para verificar
	#datos
	return render(request,"registros/formEditarComentario.html",
		{'comentario':comentario})


