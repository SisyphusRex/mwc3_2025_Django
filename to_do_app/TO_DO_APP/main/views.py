from django.shortcuts import render
from django.http import HttpResponse
from main.models import Todo


def index(request):
    """shows main page"""
    # obj = Todo.objects.create(
    #     item_name="test",
    #     description="to test",
    #     start_date="2025-03-22",
    #     start_time="14:28:00",
    #     end_date="2025-03-23",
    #     end_time="12:00:00",
    # )
    data = Todo.objects.all()
    return render(request, "main/index.html", {"data": data})


def add(request):
    """add new todo object to list"""
    ...


def delete(request):
    """delete object from database"""

    data = Todo.objects.all()
    return render(request, "main/index.html", {"data": data})
