from typing import List, Optional

from eshop.business_logic.product import Product


_products: List[Product] = [
    Product(
        id='1',
        name='TV',
        price=15
    ),
    Product(
        id='2',
        name='Cofeemachine',
        price=10
    ),
    Product(
        id='3',
        name='Laptop',
        price=12
    )
]


def save(product: Product):
    if product.id == "0":
        product.id = str(max([int(p.id) for p in _products]) + 1)
        _products.append(product)
    else:
        for i in range(len(_products)):
            existed_product = _products[i]
            if existed_product.id == product.id:
                _products[i] = product
                break

        else:
            _products.append(product)


def delete_by_id(id: str):
    global _products
    _products = [p for p in _products if p.id != id]


def get_by_id(id: str) -> Optional[Product]:
    return next((p for p in _products if p.id == id), None)


def get_many(page: int = 0, limit: int = 10):
    start = page * limit
    end = start + limit
    return _products[start:end]
