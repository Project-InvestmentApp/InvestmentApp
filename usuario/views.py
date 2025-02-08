from django.shortcuts import render, redirect

# Create your views here.
app_name = 'usuario'


def index(request):

    return render(
        request,
        'index.html',
    )