from inventory_report.inventory.product import Product


def test_cria_produto():
    """Testa criar um novo produto com atributos corretamente preenchidos"""
    mocked_product = Product(
        "01",
        "Suco de Pera",
        "SehLoiro inc",
        "18/04/2015",
        "10/03/2021",
        "FON01",
        "Manter em lugar gelado",
    )

    assert mocked_product.id == "01"
    assert mocked_product.nome_do_produto == "Suco de Pera"
    assert mocked_product.nome_da_empresa == "SehLoiro inc"
    assert mocked_product.data_de_fabricacao == "18/04/2015"
    assert mocked_product.data_de_validade == "10/03/2021"
    assert mocked_product.numero_de_serie == "FON01"
    assert (
        mocked_product.instrucoes_de_armazenamento == "Manter em lugar gelado"
    )
