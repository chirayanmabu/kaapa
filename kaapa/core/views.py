from django.shortcuts import render
from django.http import HttpResponse


def registerPage(request):
    context = {

    }
    return render(request, '/accounts/register.html', context)
