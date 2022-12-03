from django.shortcuts import render

def thing(request):
    return render(request, 'things.html')