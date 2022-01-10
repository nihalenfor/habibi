from django.shortcuts import render

# Create your views here.


def Build(request):
    return render(request, 'tower.html')