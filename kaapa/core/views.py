from django.shortcuts import render
from django.http import HttpResponse


def registerPage(request):
    context = {
    }
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    context = {

    }
    return render(request, 'accounts/login.html', context)


def homePage(request):
    context = {

    }
    return render(request, 'accounts/index.html', context)
    # return HttpResponse('hello')
