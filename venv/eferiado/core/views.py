from django.shortcuts import render
from datetime import date



def natal(resquest):
    hoje = date.today()
    natal = hoje.month == 12 and hoje.day == 25
    tiradentes = hoje.month == 4 and hoje.day == 21
    contexto = {'natal': natal, 'tiradentes': tiradentes}
    return render(resquest, 'natal.html', contexto)
    




