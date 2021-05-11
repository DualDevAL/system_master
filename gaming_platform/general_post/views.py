from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.decorators import login_required
#--------------------------------------------------------------------------
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import Postform
from django.contrib.messages.context_processors import messages
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import HttpResponsePermanentRedirect
from django.urls import reverse


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'


class AddGameView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = Postform
    template_name = 'post/post_new.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente da venda atualizada com sucesso!')
        return reverse_lazy('home')




        
        
        
