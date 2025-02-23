from django.http import HttpResponse  # ✅ Добавить это
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict[str, any] = {
        'titel': 'Home',
        'content': 'Создание интернет магазина на python c Django 4 с нуля | Часть 1',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse('About page')
