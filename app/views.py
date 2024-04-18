from django.shortcuts import render, redirect
from .form import FormImage
from .models import Image
from .funcitons import validaCpf, pegarCpfImagem

def index(request):
    if request.method == 'POST':
        form = FormImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            urlImage = Image.objects.last().image
            
            cpf = pegarCpfImagem(str(urlImage))
            validador = validaCpf(cpf)
            return render(request, 'app/image.html', {'cpf':cpf, 'validador':validador})
    else:
        form = FormImage()
        return render(request, 'app/index.html', {'form':form})

def new_image(request):
    if request.method == 'POST':
        form = FormImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            urlImage = Image.objects.last().image
            cpf = pegarCpfImagem(str(urlImage))
            validador = validaCpf(cpf)
            return render(request, 'app/image.html', {'cpf':cpf, 'validador':validador})
    else:
        form = FormImage()
        return render(request, 'app/image.html', {'form':form})
    
def teste_image(request):
    return render(request, 'app/image.html')