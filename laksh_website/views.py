from django.shortcuts import render

def homepage(request):
    # We will create this 'index.html' file next
    return render(request, 'index.html')