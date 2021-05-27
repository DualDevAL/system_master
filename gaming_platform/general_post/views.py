from django.contrib.messages.api import success
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Designer, Player, Post, GameCategory, Publisher, Age_Range, Operational_System\
    ,Graphics_Engine, Select_Language, MinimumRequirements, RecommendedRequirements

#--------------------------------------------------------------------------
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import Postform
from django.contrib.messages.context_processors import messages
from django.urls import reverse_lazy
from django.contrib import messages
from easy_pdf.views import PDFTemplateResponseMixin

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


class GameUpdateView(UpdateView):
    model = Post
    form_class = Postform
    template_name = 'post/post_edit.html'

    def get_success_url(self):
        messages.success(self.request, 'Jogo Alterado com sucesso!')
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

class CategoryUpdateView(UpdateView):
    model = GameCategory
    template_name = 'category/category_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
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


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher/publisher_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
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


class AgeUpdateView(UpdateView):
    model = Age_Range
    template_name = 'age/age_edit.html'
    fields = ["age", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
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


class SystemUpdateView(UpdateView):
    model = Operational_System
    template_name = 'system/system_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
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



class EngineUpdateView(UpdateView):
    model = Graphics_Engine
    template_name = 'engine/engine_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
        return reverse_lazy('home_engine')

# ================= CLASS DESIGNER ==================================

class DesignerListView(ListView):
    model = Designer
    template_name = 'designer/home_designer.html'


class DesignerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Designer
    template_name = 'designer/designer_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_designer')



class DesignerUpdateView(UpdateView):
    model = Designer
    template_name = 'designer/designer_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
        return reverse_lazy('home_designer')

# ================= CLASS LANGUAGE ==================================

class Select_LanguageListView(ListView):
    model = Select_Language
    template_name = 'language/home_language.html'


class Select_LanguageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Select_Language
    template_name = 'language/language_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_language')



class Select_LanguageUpdateView(UpdateView):
    model = Select_Language
    template_name = 'language/language_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
        return reverse_lazy('home_language')


# ================= CLASS REQUERIMENTOS MÍNIMOS ==================================

class MinimumRequirementsListView(ListView):
    model = MinimumRequirements
    template_name = 'min_requirements/home_min_requirements.html'


class MinimumRequirementsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MinimumRequirements
    template_name = 'min_requirements/min_requirements_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_min_requirements')



class MinimumRequirementsUpdateView(UpdateView):
    model = MinimumRequirements
    template_name = 'min_requirements/min_requirements_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
        return reverse_lazy('home_min_requirements')

# ================= CLASS REQUERIMENTOS REDOMENDADOS ==================================

class RecommendedRequirementsListView(ListView):
    model = RecommendedRequirements
    template_name = 'max_requirements/home_max_requirements.html'


class RecommendedRequirementsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = RecommendedRequirements
    template_name = 'max_requirements/max_requirements_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_max_requirements')



class RecommendedRequirementsUpdateView(UpdateView):
    model = RecommendedRequirements
    template_name = 'max_requirements/max_requirements_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
        return reverse_lazy('home_max_requirements')

# ================= CLASS JOGADORES ==================================

class PlayerListView(ListView):
    model = Player
    template_name = 'player/home_player.html'


class PlayerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Player
    template_name = 'player/player_new.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'adicionado com sucesso!')
        return reverse_lazy('home_player')



class PlayerUpdateView(UpdateView):
    model = Player
    template_name = 'player/player_edit.html'
    fields = ["name", "description", "status" ]

    def get_success_url(self):
        messages.success(self.request, 'Alterado com sucesso!')
        return reverse_lazy('home_player')


#================= PDF ==================================
class SalePDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Post
    template_name = 'detail/receipt_pdf.html'