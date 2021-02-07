from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    #data = models.DateTimeField(auto_now_add=True) # add automatically Date of NOW
    #data = models.DateTimeField(auto_now=True)     # Show Today to be add to DB
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #observacoes = models.TextField()               # It is compulsonry filling observacoes field. False, for next line of code
    observacoes = models.TextField(null=True, blank=True)   # null here let us create table where filling observacoes become optional

    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self):
        return self.descricao
