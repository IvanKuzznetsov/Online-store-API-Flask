from marshmallow import Schema, fields


class OrderHttpDto(Schema):
    class Meta:
        fields = ["id", "product_ids", "total"]

    id = fields.String()
    product_ids = fields.List(fields.Str())
    total = fields.Float()


class OrderCreateHttpBodySchema(Schema):
    product_ids = fields.List(fields.Str(), required=True)


class OrderGetParamsSchema(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)
