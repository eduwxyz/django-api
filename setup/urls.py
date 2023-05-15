from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from loja.views import (
    ClientesViewSet,
    ProdutosViewSet,
    PedidosViewSet,
    ListaPedidoCliente,
)

router = routers.DefaultRouter()
router.register("produtos", ProdutosViewSet, basename="produtos")
router.register("clientes", ClientesViewSet, basename="clientes")
router.register("pedidos", PedidosViewSet, basename="pedidos")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("cliente/<int:pk>/pedidos/", ListaPedidoCliente.as_view()),
]
