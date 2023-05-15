from rest_framework import generics, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from loja.models import Cliente, Pedido, Produto
from serializer import (
    ClienteSerializer,
    ListaPedidoClienteSerializer,
    PedidoSerializer,
    ProdutoSerializer
)


class ProdutosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os produtos
    """

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    parser_classes = (JSONParser, XMLParser)
    renderer_classes = (JSONRenderer,XMLRenderer)
    http_method_names = ['get', 'post', 'put', 'delete']


class ClientesViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os clientes
    """

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    parser_classes = (JSONParser,XMLParser)
    renderer_classes = (JSONRenderer,XMLRenderer)
    http_method_names = ['get', 'post', 'put', 'delete']


class PedidosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os pedidos
    """

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    parser_classes = (JSONParser,XMLParser)
    renderer_classes = (JSONRenderer,XMLRenderer)
    http_method_names = ['get', 'post', 'put', 'delete']


class ListaPedidoCliente(generics.ListAPIView):
    """
    Listando os pedidos dos clientes
    """

    def get_queryset(self):
        queryset = Pedido.objects.filter(cliente=self.kwargs["pk"])
        return queryset

    serializer_class = ListaPedidoClienteSerializer
    parser_classes = (JSONParser,XMLParser)
    renderer_classes = (JSONRenderer, XMLRenderer)
    http_method_names = ['get', 'post', 'put', 'delete']
    
    
