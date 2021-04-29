from django.shortcuts import render
from django.views.generic import ListView
from . models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def hello(request):
    return HttpResponse('olá mundo')

class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'
