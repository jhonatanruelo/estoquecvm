from django.db import models
from django.urls import reverse_lazy


class Produto(models.Model):
    produto = models.CharField(max_length=100, unique=True)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)
    data = models.DateField(null=True, blank=True)
    local = models.ForeignKey('Local', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }


class Local(models.Model):
    local = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('local',)

    def __str__(self):
        return self.local
