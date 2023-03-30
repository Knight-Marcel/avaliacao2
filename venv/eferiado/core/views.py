from django.shortcuts import render

from django.http import HttpResponse
def natal(request):
    contexto = {'carnaval': True,
        'natal': False}
    return render(request, 'natal.html', contexto)
