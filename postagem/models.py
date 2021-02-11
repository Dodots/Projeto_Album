from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Postagem(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField()
    data_postagem = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Data da Postagem")
    foto_postagem = models.FileField()
    publicada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, default="1")

    def __str__(self):
        return "{} ({}) - {}" .format(self.titulo, self.descricao, self.foto_postagem)