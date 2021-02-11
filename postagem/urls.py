from django.urls import path
from .views import PostagemCreateView, PostagemUpdateView, PostagemDeleteView ,PostagensListView, PostagemDetailView, DashboardListView

urlpatterns = [
    path('', PostagensListView.as_view(), name='index'),
    path('add-post', PostagemCreateView.as_view(), name='add-post'),
    path('editar-post/<int:pk>', PostagemUpdateView.as_view(), name='editar-post'),
    path('excluir-post/<int:pk>', PostagemDeleteView.as_view(), name='excluir-post'),
    path('postagem/<int:pk>', PostagemDetailView.as_view(), name='postagem'),
    path('dashboard', DashboardListView.as_view(), name='dashboard'),
]