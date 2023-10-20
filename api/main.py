from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
# from models import User, SessionLocal, engine
# from database.query import query_get, query_put, query_update
# from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from user import *
from check_api_key import *
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:4000",
    "http://localhost:19006"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



################################
########## Users APIs ##########
################################

@app.post("/users/", response_model=User)
def create_user(user: User, db: Session = Depends(SessionLocal),
                api_key: str = Depends(check_api_key)):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/v1/users" , response_model=list[User])
def get_all_users( skip: int = 0, limit: int = 100,
                   db: Session = Depends(SessionLocal),api_key: str = Depends(check_api_key)):
    """
    This users get API allow you to fetch all user data.
    """
 
    users = db.query(User).offset(skip).limit(limit).all()
    return users
    


@app.get("/v1/users/{user_id}", response_model=User)
def get_user(user_id: int,  db: Session = Depends(SessionLocal),
                 api_key: str = Depends(check_api_key)):
    """
    This user API allow you to fetch specific user data.
    """
     
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

     


@app.put("/v1/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User,   db: Session = Depends(SessionLocal), api_key: str = Depends(check_api_key)):
    """
    This user update API allow you to update user data.
    """
    
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for attr, value in user.dict().items():
        setattr(db_user, attr, value)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(SessionLocal)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user

################################
########## Product APIs ##########
################################

# @app.post('/v1/product', response_model=ProductResponseModel)
# def create_product(product_details: ProductResponseModel):
#     """
#     This sign-up API allow you to register your account, and return access token.
#     """
#     product = register_product(product_details)
   
#     return JSONResponse(status_code=200, content=jsonable_encoder(product))


# @app.get("/v1/products", response_model=list[ProductResponseModel])
# def get_all_products(api_key: str = Depends(check_api_key)):
#     """
#     This products get API allow you to fetch all product data.
#     """
 
#     products = get_all_products()
#     return JSONResponse(status_code=200, content=jsonable_encoder(products))
     

###############################
########## Test APIs ##########
###############################

# @app.get('/secret')
# def secret_data(api_key: str = Depends(check_key)):
#     """
#     This secret API is just for testing. Need access token to access this API.
#     """
#     token = credentials.credentials
#     if (auth_handler.decode_token(token)):
#         return 'Top Secret data only authorized users can access this info'


# @app.get('/not-secret')
# def not_secret_data():
#     """
#     This not-secret API is just for testing.
#     """
#     return 'Not secret data'

# Define a route and apply the check_key dependency
@app.get("/secure-endpoint/")
async def secure_endpoint(api_key: str = Depends(check_api_key)):
    return {"message": "This is a secure endpoint!"}