from django.shortcuts import render
from .models import Produto
from django.views.generic.list import ListView

class ProdutoList(ListView):
    model = Produto
