from django.shortcuts import render
from .models import Post, Contact


def hello_blog(request):
    list_post = Post.objects.all()
    data = {'posts': list_post}    
    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})

def save_form(request):
    name=request.POST['name']
    Contact.objects.create(
        name=name,
        email=request.POST['email'],
        message=request.POST['message']
    )
    return render(request, 'contact_sucess.html', {'name_contact':name})