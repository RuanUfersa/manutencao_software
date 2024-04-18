from rest_framework import serializers
from .models import Verduras, Frutas, Entrega, Pagamento, Item

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True

class ProdutoSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = None
        fields = ['nome', 'created_at', 'updated_at']

class VerdurasSerializer(ProdutoSerializer):
    class Meta(ProdutoSerializer.Meta):
        model = Verduras
        fields = ['nome', 'preco_da_verdura', 'quantidade_de_verdura_disponivel', 'created_at', 'updated_at']

class FrutasSerializer(ProdutoSerializer):
    class Meta(ProdutoSerializer.Meta):
        model = Frutas
        fields = ['nome', 'preco_da_fruta', 'quantidade_de_fruta_disponivel', 'created_at', 'updated_at']

class EntregaSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())

    class Meta:
        model = Entrega
        fields = ['nome_do_cliente', 'endereco_da_entrega', 'data_da_entrega', 'itens', 'pagamento', 'created_at', 'updated_at']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['modo_de_pagamento', 'valor_total_do_pagamento', 'created_at', 'updated_at']

class ItemSerializer(serializers.ModelSerializer):
    entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())

    class Meta:
        model = Item
        fields = ['nome_do_item', 'quantidade_do_item', 'preco_unitario_do_item', 'entrega', 'created_at', 'updated_at']
