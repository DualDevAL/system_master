from django.forms import ModelForm, CharField
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Post


class Postform(ModelForm):
    conteudo = CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ("titulo", "categoria", "conteudo", "imagem", "status")
