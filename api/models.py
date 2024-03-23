from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Product(Model):
    id = fields.IntField(pk=True)
    p_name = fields.CharField(max_length=55, nullable=False )
    quantity = fields.IntField(default=0)
    quantity_sold=fields.IntField(default=0)
    unit_price = fields.IntField(default=0)
    revenue = fields.IntField(default=0)
    supplied_by = fields.ForeignKeyField('models.Supplier',related_name='goods_supplied')


class Supplier(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=55 )
    company = fields.CharField(max_length=20)
    email = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=15)


product_pydantic = pydantic_model_creator(Product, name="Product")
product_pydanticIn = pydantic_model_creator(Product, name="ProductIn", exclude_readonly=True)

supplier_pydantic = pydantic_model_creator(Supplier, name="Supplier")
supplier_pydanticIn = pydantic_model_creator(Supplier, name="SupplierIn", exclude_readonly=True)
