from typing import Optional, List

from eshop.business_logic.product import Product
from eshop.data_access.product_repo import save, get_many, get_by_id


def product_create(dto) -> Product:

    product = Product(
            id="0",
            name=dto["name"],
            price=dto["price"]
        )

    save(product)
    return product


def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)

