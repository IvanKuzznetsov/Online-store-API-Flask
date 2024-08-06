from flask import Flask, request
from marshmallow import ValidationError

from eshop.business_logic.order import Order
from eshop.business_logic.order_usecases import order_get_many, order_get_by_id, order_create
from eshop.business_logic.product_usecases import product_create, product_get_many, product_get_by_id
from eshop.view.order_schemas import OrderGetParamsSchema, OrderCreateHttpBodySchema, OrderHttpDto
from eshop.view.products_schemas import ProductCreateHttpBodySchema, ProductHttpDto, ProductGetParamsSchema

app = Flask(__name__)


@app.post('/api/v1/order')
def order_create_controller():
    try:
        dto = OrderCreateHttpBodySchema().load(request.json)
    except ValidationError as err:
        return {
            "errors": err.messages
        }, 400

    try:
        order = order_create(product_ids=dto["product_ids"])
    except Exception as err:
        return {
            "message": str(err)
        }, 400

    return OrderHttpDto().dump(order)


@app.post('/api/v1/product')
def product_create_controller():
    try:
        dto = ProductCreateHttpBodySchema().load(request.json)
    except ValidationError as err:
        return {
            "errors": err.messages
        }, 400

    try:
        product = product_create(dto)
    except Exception as err:
        return {
            "message": str(err)
        }, 400

    return ProductHttpDto().dump(product)


@app.get('/api/v1/order/<id>')
def order_get_by_id_controller(id: str):
    order = order_get_by_id(id)
    if order is None:
        return {
            "message": "Order not found"
        }, 404
    return OrderHttpDto().dump(order)


@app.get('/api/v1/product/<id>')
def product_get_by_id_controller(id: str):
    product = product_get_by_id(id)
    if product is None:
        return {
            "message": "Product not found"
        }, 404
    return ProductHttpDto().dump(product)


@app.get('/api/v1/order')
def order_get_many_controller():
    try:
        params = OrderGetParamsSchema().load(request.args)
    except ValidationError as err:
        return {
            "errors": err.messages
        }, 400

    page = params["page"]
    limit = params["limit"]

    orders = order_get_many(page, limit)
    return OrderHttpDto(many=True).dump(orders)


@app.get('/api/v1/product')
def product_get_many_controller():
    try:
        params = ProductGetParamsSchema().load(request.args)
    except ValidationError as err:
        return {
            "errors": err.messages
        }, 400

    page = params["page"]
    limit = params["limit"]

    products = product_get_many(page, limit)
    return ProductHttpDto(many=True).dump(products)


def run_server():
    app.run(port=5000)
