from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoListCreateApiView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        nome = serializer.validated_data.get('nome')
        preco = serializer.validated_data.get('preco')
        serializer.save(nome=nome, preco=preco)


class ProdutoDetailAPIView(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_field = 'pk'


class ProdutoUpdateAPIView(generics.UpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


class ProdutoDestroyAPIView(generics.DestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
