from django.shortcuts import render

def hello_blog(request):
    return render(request, 'index_all.html')
