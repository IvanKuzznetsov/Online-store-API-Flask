import uuid
from typing import List

from eshop.business_logic.order import Order
from eshop.data_access.order_repo import get_by_id, get_many, save
from eshop.data_access.product_repo import get_by_id as product_get_by_id


def order_create(product_ids: List[str]) -> Order:
    products = []
    for id in product_ids:
        product = product_get_by_id(id)
        if product is None:
            raise Exception(f'Product with id {id} not exists')

        products.append(product)

    total = sum(p.price for p in products)
    order = Order(
        id=str(uuid.uuid4()),
        product_ids=product_ids,
        total=total
    )
    save(order)

    return order


def order_get_by_id(id: str) -> Order:
    return get_by_id(id)


def order_get_many(page: int, limit: int) -> List[Order]:
    return get_many(page=page, limit=limit)
