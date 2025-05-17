from django.http import HttpResponse
from django.shortcuts import render


def students(request):
    students = [{"id": 1, "name": "Jhon", "age": 25}]
    return HttpResponse(students)
