from django.shortcuts import render
from .models import Post 

display_image = "https://images.unsplash.com/photo-1554744512-d6c603f27c54?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"

def home(request):
    context_dict = { 'posts': Post.objects.all() , "image": display_image }
    return render(request, 'blog/home.html', context_dict)

def about(request):
    return render(request, 'blog/about.html', { 'title' : 'About' })


