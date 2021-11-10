from django.db import models
from django_ckeditor_5 import forms
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    """ Articles for blog. """
    text1 = CKEditor5Field("Text1", config_name='default', null=True, blank=True)
    text2 = CKEditor5Field("Text2", config_name='default', null=True, blank=True)
    text3 = CKEditor5Field("Text3", config_name='default', null=True, blank=True)
    text4 = CKEditor5Field("Text4", config_name='default', null=True, blank=True)
    text5 = CKEditor5Field("Text5", config_name='default', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Articles"
        verbose_name = "article"


class ArticleForm(forms.forms.ModelForm):
    class Meta:
        model = Article
        fields = ['text1', 'text2', 'text3', 'text4', 'text5']
