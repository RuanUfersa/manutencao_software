from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Verduras(Produto):
    preco_da_verdura = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_de_verdura_disponivel = models.IntegerField()
    class Meta:
        verbose_name = "Verdura"
        verbose_name_plural = "Verduras"

    def __str__(self):
        return f'{self.nome}'

class Frutas(Produto):
    preco_da_fruta = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_de_fruta_disponivel = models.IntegerField()
    class Meta:
        verbose_name = "Fruta"
        verbose_name_plural = "Frutas"

    def __str__(self):
        return f'{self.nome}'

class Entrega(Base):
    nome_do_cliente = models.CharField(max_length=255)
    endereco_da_entrega = models.TextField()
    data_da_entrega = models.DateTimeField()

class Pagamento(Base):
    modo_de_pagamento = models.CharField(max_length=50)
    valor_total_do_pagamento = models.DecimalField(max_digits=8, decimal_places=2)

class Item(Base):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nome_do_item = models.CharField(max_length=100)
    quantidade_do_item = models.IntegerField()
    preco_unitario_do_item = models.DecimalField(max_digits=6, decimal_places=2)

