from django.shortcuts import render
from .models import Feriado, Aula
from datetime import date, timedelta

def get_month_days(year, month):
    """Retorna uma lista com todos os dias do mês especificado."""
    first_day = date(year, month, 1)
    days_in_month = (first_day.replace(month=month % 12 + 1, day=1) - timedelta(days=1)).day
    return [first_day + timedelta(days=i) for i in range(days_in_month)]

def home_calendar(request):
    today = date.today()
    month_days = get_month_days(today.year, today.month)
    feriados = {f.data: f for f in Feriado.objects.filter(data__month=today.month)}
    return render(request, 'calendar/home_calendar.html', {
        'month_days': month_days,
        'feriados': feriados,
    })

def filtered_calendar(request):
    today = date.today()
    month_days = get_month_days(today.year, today.month)
    feriados = {f.data: f for f in Feriado.objects.filter(data__month=today.month)}
    aulas = {a.data: a for a in Aula.objects.filter(data__month=today.month)}
    return render(request, 'calendar/filtered_calendar.html', {
        'month_days': month_days,
        'feriados': feriados,
        'aulas': aulas,
    })
