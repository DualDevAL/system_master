from django.contrib.messages.api import success
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post, GameCategory, Publisher, Age_Range, Operational_System\
    ,Graphics_Engine

#--------------------------------------------------------------------------
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import Postform
from django.contrib.messages.context_processors import messages
from django.urls import reverse_lazy
from django.contrib import messages

# =================== Templates secudary ===============================
class AtributesListView(ListView):
    model = Post
    template_name = 'post/post_atributes.html'


# ======================== CLASS POST ==================================
class GameListView(ListView):

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


class GameUpdateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = Postform
    template_name = 'post/post_edit.html'

    def get_success_url(self):
        messages.success(self.request, 'Jogo adicionado com sucesso!')
        return reverse_lazy('home')


class CancelarDeleteView(ListView):
    model = GameCategory
    template_name = 'post/home.html'


# ================= CLASS GAMECATEGORY ==================================

class CategoryListView(ListView):
    model = GameCategory
    template_name = 'category/home_category.html'


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = GameCategory
    template_name = 'category/category_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_category')

# ================= CLASS PUBLISHER ==================================

class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher/home_publisher.html'


class PublisherCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Publisher
    template_name = 'publisher/publisher_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_publisher')

# ================= CLASS AGERANGE ==================================

class AgeListView(ListView):
    model = Age_Range
    template_name = 'age/home_age.html'


class AgeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Age_Range
    template_name = 'age/age_new.html'
    fields = ["age", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_age')

# ================= CLASS OPERATIONA_SYSTEM ==================================

class SystemListView(ListView):
    model = Operational_System
    template_name = 'system/home_system.html'


class SystemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Operational_System
    template_name = 'system/system_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_system')

# ================= CLASS GRAPHICS_ENGINE ==================================

class EngineListView(ListView):
    model = Graphics_Engine
    template_name = 'engine/home_engine.html'


class EngineCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Graphics_Engine
    template_name = 'engine/engine_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_engine')


