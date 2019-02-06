from django.shortcuts import (render,
                              redirect,
                              get_object_or_404
                              )
from .models import Articles
from django.contrib.auth.decorators import login_required
from . import forms


def python_list(request):
    articles = Articles.objects.filter(category=1)
    return render(request, 'articles/articles.html', {'articles': articles})


def blog_list(request):
    articles = Articles.objects.filter(category=2)
    return render(request, 'articles/articles.html', {'articles': articles})


def full_article(request, id):
    # article = Articles.objects.get(id=id)
    article = get_object_or_404(Articles, id=id)
    return render(request, 'articles/fullarticle.html', {'article': article})


@login_required()
def writeblog(request):
    if request.method == 'POST':
        form = forms.Writeform(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Writeform()
    return render(request, 'articles/writeblog.html', {'form': form})


@login_required()
def update_view(request, id):
    article = get_object_or_404(Articles, id=id)
    if request.method == 'POST':
        form = forms.Writeform(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return render(request, 'articles/fullarticle.html', {'article': article})
    form = forms.Writeform(instance=article)
    context = {'form': form,
               'article': article}
    return render(request, 'articles/updateblog.html', context)


def delete_view(request, id):
    Articles.objects.get(id=id).delete()
    return redirect('home')
