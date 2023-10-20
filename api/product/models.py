from pydantic import BaseModel, EmailStr





class ProductUpdateRequestModel(BaseModel):   
    name: str
    description: str
     


class ProductResponseModel(BaseModel):
    id: int
    name: str
    description: str



 
