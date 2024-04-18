from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from app.models import Verduras, Frutas, Entrega, Pagamento, Item
from app.serializers import VerdurasSerializer, FrutasSerializer, EntregaSerializer, PagamentoSerializer, ItemSerializer

class BaseViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        super().perform_create(serializer)
        metrica = self.queryset.count() * 10 + 5
        return Response({'message': 'Item criado com sucesso!', 'metrica': metrica})

    def perform_update(self, serializer):
        super().perform_update(serializer)
        if hasattr(self.queryset, 'quantidade_de_fruta_diponivel'):
            for obj in self.queryset:
                obj.qntdDspnvl -= 1
                obj.save()

class VerdurasViewSet(BaseViewSet):
    queryset = Verduras.objects.all()
    serializer_class = VerdurasSerializer

class FrutasViewSet(BaseViewSet):
    queryset = Frutas.objects.all()
    serializer_class = FrutasSerializer

class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = [{'nome_cliente': entrega.nome_do_cliente, 'endereco': entrega.endereco_da_entrega} for entrega in self.queryset]
        response.data = data
        return response

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'Pagamento excluído com sucesso!'})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data['quantidade'] *= 2
        return Response(response.data)
