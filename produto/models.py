from django.db import models

CATEGORIA_CHOICES = [
    ('CER', 'cerveja'),
    ('REF', 'refrigerante'),
    ('SUC', 'suco'),
]

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=3)
    estoque_inicial = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=0)
