from rest_framework import serializers

from loja.models import Cliente, Pedido, Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ("id", "nome", "preco", "estoque")


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ("id", "nome", "sobrenome", "email")


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ("id", "cliente", "produto", "quantidade", "valor", "data")


class ListaPedidoClienteSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model = Pedido
        fields = ("produto", "quantidade", "data")
        
        