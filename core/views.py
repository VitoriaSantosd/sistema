from django.shortcuts import render
from .models import Feriado, Aula
from datetime import date

def calendario_geral(request):
    feriados = Feriado.objects.all()
    return render(request, 'calendario_geral.html', {'feriados': feriados})

def calendario_filtrado(request):
    curso = request.GET.get('curso')
    periodo = request.GET.get('periodo')
    turno = request.GET.get('turno')
    
    aulas = Aula.objects.filter(curso=curso, turno=turno, periodo=periodo)
    feriados = Feriado.objects.all()

    return render(request, 'calendario_filtrado.html', {'aulas': aulas, 'feriados': feriados})
    
def atualizar_aulas(request):
    if request.method == "POST":
        aula_id = request.POST.get("update_aula")
        if aula_id:
            aula = Aula.objects.get(id=aula_id)
            aula.data = request.POST.get(f"data_{aula_id}")
            aula.status = request.POST.get(f"status_{aula_id}")
            aula.save()
            return redirect("atualizar_aulas")  

    aulas = Aula.objects.all()
    return render(request, "atualizar_aulas.html", {"aulas": aulas})