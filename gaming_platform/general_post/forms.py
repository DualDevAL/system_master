from django.forms import ModelForm, CharField
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Post


class Postform(ModelForm):
    description = CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ("title" , "publisher", "genre", "description", "image", "value", "status")

