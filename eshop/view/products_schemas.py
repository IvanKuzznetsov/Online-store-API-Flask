from marshmallow import Schema, fields


class ProductHttpDto(Schema):
    class Meta:
        fields = ["id", "name", "price"]

    id = fields.String()
    name = fields.String()
    price = fields.Int()


class ProductCreateHttpBodySchema(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)


class ProductGetParamsSchema(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)
