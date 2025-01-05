from django.shortcuts import render

# Create your views here.

def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    return render(request, 'fourth_task/games.html')


def cart(request):
    return render(request, 'fourth_task/cart.html')

