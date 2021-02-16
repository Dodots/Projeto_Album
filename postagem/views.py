from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Postagem
from django.urls import reverse_lazy

class PostagemCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Postagem
    fields = ['titulo', 'descricao', 'foto_postagem']
    template_name = 'postagem/form-upload.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
       
        return url

class PostagemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Postagem
    fields = ['titulo', 'descricao', 'foto_postagem']
    template_name = 'postagem/form-upload.html'
    success_url = reverse_lazy('dashboard')

class PostagemDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Postagem
    template_name = 'postagem/form-excluir.html'
    success_url = reverse_lazy('dashboard')

class PostagensListView(ListView):
    model = Postagem
    template_name = 'postagem/index.html'
    context_object_name = "postagem_list"
    paginate_by = 6 

    def get_queryset(self, **kwargs):
        return Postagem.objects.filter(publicada=True).order_by('-data_postagem')


class PostagemDetailView(DetailView):
    model = Postagem
    template_name = 'postagem/postagem.html'

class DashboardListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Postagem
    template_name = 'usuario/dashboard.html'

    def get_queryset(self):
        self.object_list = Postagem.objects.filter(usuario=self.request.user)
        return self.object_list

