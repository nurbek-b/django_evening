from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .forms import PostForm, PostEditForm
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostEditForm


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
