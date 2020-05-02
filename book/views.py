from django.shortcuts import render

def empty_view(request):
    return render(request, 'base.html')
