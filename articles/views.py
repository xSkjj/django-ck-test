from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article, ArticleForm


class ArticleListView(ListView):
    model = Article
    paginate_by = 100  # if pagination is desired


class ArticleDetailView(DetailView):
    model = Article


def landing(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, "landing.html", {"form": form})
    elif request.method == "POST":
        form = ArticleForm(request.POST)
        form.save()
        return redirect("/list/")
