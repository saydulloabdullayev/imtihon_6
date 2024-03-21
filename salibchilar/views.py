from django.shortcuts import render
from .models import Salib

def salib_list(request):
    saliblar = Salib.objects.all()
    return render(request, 'salibchilar/salib_list.html', {'saliblar': saliblar})





from django.shortcuts import render, redirect
from .models import Theme

def theme_list(request):
    themes = Theme.objects.all()
    return render(request, 'crud/theme_list.html', {'themes': themes})

def theme_detail(request, pk):
    theme = Theme.objects.get(pk=pk)
    return render(request, 'crud/theme_detail.html', {'theme': theme})

def theme_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Theme.objects.create(title=title, description=description)
        return redirect('theme_list')
    return render(request, 'crud/theme_form.html')

def theme_update(request, pk):
    theme = Theme.objects.get(pk=pk)
    if request.method == 'POST':
        theme.title = request.POST.get('title')
        theme.description = request.POST.get('description')
        theme.save()
        return redirect('theme_list')
    return render(request, 'crud/theme_form.html', {'theme': theme})

def theme_delete(request, pk):
    theme = Theme.objects.get(pk=pk)
    theme.delete()
    return redirect('theme_list')


def salib_bir(request):
    return render(request, 'salibchilar/salib_bir.html')

def salib_ikki(request):
    return render(request, 'salibchilar/salib_ikki.html')

def salib_umumiy(request):
    return render(request, 'salibchilar/salib_umumiy.html')


def salib_uch(request):
    return render(request, 'salibchilar/salib_uch.html')