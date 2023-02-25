from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def dinamico(request, name):
    context = { 'name': name }
    return render(request, 'dinamico.html', context)