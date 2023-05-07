from typing import Optional
from uuid import uuid4 as uuid

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[str]
    name: str
    purchase_price: float
    sale_price: float
    supplier: str

app = FastAPI()

products = []

@app.get('/')
def index():
    return {'example':'crud'}

# list product

@app.get('/product')
def list_product():
    return products

# add product

@app.post('/product')
def add_product(product:Product):
    product.id = str(uuid())
    products.append(product)
    return {'message':'product add sasticfatory'}

# search product

@app.get('/product/{product_id}')
def search_product_id(product_id:str):
    result = list(filter(lambda p:p.id == product_id, products))

    if len(result):
        return result[0]
    
    raise HTTPException(status_code=404, detail=f'the product wich id {product_id} was not found')


# delete product

@app.delete('/product/{product_id}')
def delete_product_id(product_id:str):
    result = list(filter(lambda p:p.id == product_id, products))

    if len(result):
        product = result[0]
        products.remove(product)

        return {'message':f'the product wich id {product_id} has been removed '}
    
    raise HTTPException(status_code=404, detail=f'the product wich id {product_id} was not found')

# update product

@app.put('/product/{product_id}')
def update_product(product_id:str, product:Product):
    result = list(filter(lambda p:p.id == product_id, products))

    if len(result):
        product_found = result[0]
        product_found.name = product.name
        product_found.purchase_price = product.purchase_price
        product_found.sale_price = product.sale_price
        product_found.supplier = product.supplier

        return product_found
        
    
    raise HTTPException(status_code=404, detail=f'the product wich id {product_id} was not found')
