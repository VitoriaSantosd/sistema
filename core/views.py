from django.shortcuts import render
from .models import Aula, Feriado
from .models import CalendarioGeral,  CalendarioFiltrado
# Create your views here.

def calendario_geral(request):
    feriados = Feriado.objects.all()
    aulas = Aula.objects.all()
    context = {
        'feriados': feriados,
        'aulas': aulas
    }
    return render(request, 'calendario_geral.html', context)

def calendario_filtrado(request):
    curso = request.GET.get('curso')
    periodo = request.GET.get('periodo')
    turno = request.GET.get('turno')

    aulas = Aula.objects.filter(
        curso__nome=curso,
        periodo__numero=periodo,
        turno__nome=turno
    )

    feriados = Feriado.objects.all()
    context = {
        'feriados': feriados,
        'aulas': aulas,
        'curso': curso,
        'periodo': periodo,
        'turno': turno
    }
    return render(request, 'calendario_filtrado.html', context)


def calendario_geral_view(request):
    eventos_geral = CalendarioGeral.objects.all()
    return render(request, 'calendario_geral.html', {
        'eventos_geral': eventos_geral
    })

def calendario_filtrado_view(request):
    eventos_filtro = CalendarioFiltrado.objects.all()
    eventos_geral = CalendarioGeral.objects.all()
    return render(request, 'calendario_filtrado.html', {
        'eventos_filtro': eventos_filtro,
        'eventos_geral': eventos_geral
    })