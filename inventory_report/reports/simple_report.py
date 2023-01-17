from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, products):
        find_oldest_fabrication = self._find_oldest_fabrication(products)
        nearest_expiration = self._find_nearest_expiration(products)
        common_company = self._find_most_common(products, "nome_da_empresa")
        return f"""Data de fabricação mais antiga: {find_oldest_fabrication}
Data de validade mais próxima: {nearest_expiration}
Empresa com mais produtos: {common_company}"""

    @staticmethod
    def _find_oldest_fabrication(products):
        fabrications = [item["data_de_fabricacao"] for item in products]
        return min(fabrications)

    @staticmethod
    def _find_most_common(list, filter):
        empresas = [item[filter] for item in list]
        most_common = Counter(empresas).most_common(1)[0]
        return most_common[0]

    @staticmethod
    def _find_nearest_expiration(products):
        expirations = []
        for item in products:
            expiration = datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d"
            )
            if expiration > datetime.now():
                expirations.append(item["data_de_validade"])
        return min(expirations)
