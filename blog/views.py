from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import redirect

from .models import *
from .forms import CommentForm


class PostList(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        return context


class PostDetail(ModelFormMixin, DetailView):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)
        context['comments'] = Comment.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        form = self.form_class(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        form.save()
        return redirect('blog:post-detail', kwargs['slug'])
