from django.shortcuts import render
from .models import Quiz,YoungDS,Sql,It_manager,Datashark,Ciphertrail,Mobilelegends

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def quizzle(request):
    data = Quiz.objects.all()
    return render(request, 'quiz.html', {'data': data})

def yds(request):
    data = YoungDS.objects.all()
    return render(request, 'yds.html', {'data': data})

def sql(request):
    data = Sql.objects.all()
    return render(request, 'sql.html', {'data': data})

def itmanager(request):
    data = It_manager.objects.all()
    return render(request, 'itm.html', {'data': data})

def datashark(request):
    data = Datashark.objects.all()
    return render(request, 'data.html', {'data': data})

def cipher(request):
    data = Ciphertrail.objects.all()
    return render(request, 'cipher.html', {'data': data})

def mobile(request):
    data = Mobilelegends.objects.all()
    return render(request, 'mobile.html', {'data': data})