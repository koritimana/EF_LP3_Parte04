from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Course
from miapp.models import Career
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def index(request):
   
    return render(request,'index.html', {
})

def carreras(request):
    return render(request,'carreras.html',{
})

def crear_curso(request):
    return render(request,'crear_curso.html',{
})
def crear_carrera(request):
    return render(request,'crear_carrera.html',{
})

def inicio(request):
    return render(request,'layout.html',{
    })

def cursos(request):
    cursos = Course.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        hour = 0
        credits = request.POST.get('credits')
        state = request.POST.get('state')

        # Validación de campos (puedes agregar más validaciones según tus necesidades)
        if not code or not name or not credits:
            messages.error(request, 'Todos los campos son obligatorios')
        else:
            course = Course(code=code, name=name, hour=0, credits=credits, state=state)
            course.save()
            messages.success(request, 'Pais agregado correctamente')

    return render(request, 'crear_curso.html')



def eliminar_curso(request, curso_id):
    course = get_object_or_404(Course, id=curso_id)
    course.delete()
    return redirect('cursos')

def listar_carreras(request):
    carreras = Career.objects.all()
    return render(request, 'carreras.html', {'carreras': carreras})

def crear_carrera(request):
    if request.method == 'POST':
        name = request.POST['name']
        shortname = request.POST['shortname']
        image = request.FILES.get('image')  # Usa request.FILES para obtener la imagen enviada

        # Obtenemos el valor del campo state como un string ('on' o None)
        state_str = request.POST.get('state', None)

        # Convertimos el string a un valor booleano válido (True o False)
        state = True if state_str == 'on' else False

        Career.objects.create(name=name, shortname=shortname, image=image, state=state)
        messages.success(request, 'Editorial agregada exitosamente.')
        return redirect('carreras')

    return render(request, 'crear_carrera.html')

def eliminar_carrera(request, carrera_id):
    carrera = get_object_or_404(Career, id=carrera_id)
    carrera.delete()
    messages.success(request, 'Editorial eliminada exitosamente.')
    return redirect('carreras')

def editar_carrera(request, carrera_id):
    carrera = get_object_or_404(Career, id=carrera_id)

    if request.method == 'POST':
        name = request.POST['name']
        shortname = request.POST['shortname']
        image = request.FILES.get('image', carrera.image)
        state = True if request.POST.get('state', False) else False

        carrera.name = name
        carrera.shortname = shortname
        carrera.image = image
        carrera.state = state
        carrera.save()

        messages.success(request, 'Editorial actualizada exitosamente.')
        return redirect('carreras')

    return render(request, 'editar_carrera.html', {'carrera': carrera})

def integrantes(request):
    return render(request,'integrantes.html',{
})