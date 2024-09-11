from django.shortcuts import render
from .models import New

def index(request):
    new = New.objects.all
    context = {"new": new}
    return render(request, "aidananews/index.html", context)

