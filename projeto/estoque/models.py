from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from django.db.models.deletion import CASCADE
from projeto.core.models import TimeStampedModel
from projeto.produto.models import Produto

from .managers import EstoqueEntradaManager, EstoqueSaidaManager

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)
    estoque_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True, related_name='NOME_DO_PRODUTO')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} --- {} --- {}'.format(self.estoque_produto, self.pk, self.created.strftime('%d-%m-%Y'))

   
class EstoqueEntrada(Estoque):

    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'


class EstoqueSaida(Estoque):

    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque saída'
        verbose_name_plural = 'estoque saída'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoques'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)



