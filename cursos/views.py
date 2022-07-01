from django.shortcuts import render

def pagina_inicial(request):
    return render(request, "/cursos/pagina_inicial.html")

def listar_cursos(request):
    return render(request, 'cursos/cursos.html')