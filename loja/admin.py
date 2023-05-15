from django.contrib import admin

from loja.models import Cliente, Produto, Pedido


class Produtos(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "estoque")
    list_display_links = ("nome", "preco", "estoque")
    search_fields = ("nome",)
    list_per_page = 10


admin.site.register(Produto, Produtos)


class Clientes(admin.ModelAdmin):
    list_display = ("id", "nome", "sobrenome", "email")
    list_display_links = ("nome", "sobrenome", "email")
    search_fields = ("nome", "sobrenome")
    list_per_page = 10


admin.site.register(Cliente, Clientes)


class Pedidos(admin.ModelAdmin):
    list_display = ("id", "cliente", "produto", "quantidade", "valor", "data")
    list_display_links = ("id",)
    search_fields = ("cliente", "produto")
    list_per_page = 10


admin.site.register(Pedido, Pedidos)

