from django.contrib.messages.api import success
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post
#--------------------------------------------------------------------------
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import Postform
from django.contrib.messages.context_processors import messages
from django.urls import reverse_lazy
from django.contrib import messages


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'


class GameCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = Postform
    template_name = 'post/post_new.html'

    def get_success_url(self):
        messages.success(self.request, 'Jogo adicionado com sucesso!')
        return reverse_lazy('home')


class GameDetaiView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class GameDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "deletado com sucesso"

    def delete(self, request, *args, **kwargs):# padrão do django
        messages.success(self.request, self.success_message)
        return super(GameDeleteView, self).delete(request, *args, **kwargs)     


class CancelarDeleteView(ListView):
    model = Post
    template_name = 'post/home.html'

