from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        find_oldest_fabrication = cls._find_oldest_fabrication(products)
        nearest_expiration = cls._find_nearest_expiration(products)
        common_company = cls._find_most_common(products, "nome_da_empresa")
        company_products = cls._quantity_products(products, "nome_da_empresa")
        return f"""Data de fabricação mais antiga: {find_oldest_fabrication}
Data de validade mais próxima: {nearest_expiration}
Empresa com mais produtos: {common_company}
Produtos estocados por empresa:
{company_products}"""

    @staticmethod
    def _quantity_products(list, filter):
        text = """"""
        companies = [item[filter] for item in list]
        count = Counter(companies).items()

        for company in count:
            name, quantity = company
            text += f"- {name}: {quantity}\n"

        return text
