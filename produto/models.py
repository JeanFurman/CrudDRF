from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nome

