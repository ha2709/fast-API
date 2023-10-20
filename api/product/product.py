from fastapi import HTTPException
from database.query import query_get, query_put, query_update
from .auth import Auth
from .models import ProductUpdateRequestModel, ProductResponseModel

auth_handler = Auth()

def register_product(product_model: ProductResponseModel):
    user = get_product_by_id(product_model.id)
    if len(user) != 0:
        raise HTTPException(
            status_code=409, detail='Product already exist.')
    
    query_put("""
                INSERT INTO product (
                    id,
                    name,
                    description
                     
                ) VALUES (%s,%s,%s)
                """,
              (
                  product_model.id,
                  product_model.name,
                  product_model.description
              
              )
              )
    user = get_product_by_id(product_model.id)
    return user[0]


def update_product(product_model: ProductUpdateRequestModel):
    hashed_password = auth_handler.encode_password(product_model.password)
    query_put("""
            UPDATE product 
                SET name = %s,
                    description = %s,
                   
                WHERE product.id = %s;
            """,
              (
                  product_model.name,
                  product_model.description,
                  
               
                
              )
              )
    products = get_product_by_id(product_model.id)
    return products[0]


def get_all_products():
    products = query_get("""
        SELECT  
            product.id,
            product.name,
            product.description
          
        FROM product
        """, ())
    return products


# def get_user_by_email(email: str):
#     user = query_get("""
#         SELECT 
#             user.id,
#             user.first_name,
#             user.last_name,
#             user.email,
#             user.password_hash
#         FROM user 
#         WHERE email = %s
#         """, (email))
#     return user


def get_product_by_id(id: int):
    product = query_get("""
        SELECT 
            product.id,
            product.name,
            product.description
             
        FROM product 
        WHERE id = %s
        """, (id))
    return product
