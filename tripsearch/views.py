from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def exchange(request):
    return render(request, 'exchange.html')

def top(request):
    return render(request, 'top.html')

# Define other views similarly...
