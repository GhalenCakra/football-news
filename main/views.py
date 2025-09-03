
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406437306',
        'name': 'Ghalen Cakra Permana',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)