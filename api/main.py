from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.middleware.cors import CORSMiddleware
from database.query import query_get, query_put, query_update
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from user import Auth, SignInRequestModel, SignUpRequestModel, UserAuthResponseModel, UserUpdateRequestModel, UserResponseModel, register_user, signin_user, update_user, get_all_users, get_user_by_id
from product import *
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

@app.get("/v1/users", response_model=list[UserResponseModel])
def get_all_users_api(api_key: str = Depends(check_api_key)):
    """
    This users get API allow you to fetch all user data.
    """
 
    user = get_all_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(user))
    


@app.get("/v1/user/{user_id}", response_model=UserResponseModel)
def get_user_api(user_id: int, api_key: str = Depends(check_api_key)):
    """
    This user API allow you to fetch specific user data.
    """
     
    user = get_user_by_id(user_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(user))
     


@app.post("/v1/user/update", response_model=UserResponseModel)
def update_user_api(user_details: UserUpdateRequestModel, api_key: str = Depends(check_api_key)):
    """
    This user update API allow you to update user data.
    """
    
    user = update_user(user_details)
    return JSONResponse(status_code=200, content=jsonable_encoder(user))
    


################################
########## Product APIs ##########
################################

@app.post('/v1/product', response_model=ProductResponseModel)
def create_product_api(product_details: ProductResponseModel):
    """
    This sign-up API allow you to register your account, and return access token.
    """
    product = register_product(product_details)
   
    return JSONResponse(status_code=200, content=jsonable_encoder(product))


@app.get("/v1/products", response_model=list[ProductResponseModel])
def get_all_products_api(api_key: str = Depends(check_api_key)):
    """
    This products get API allow you to fetch all product data.
    """
 
    products = get_all_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(products))
     

###############################
########## Test APIs ##########
###############################

# @app.get('/secret')
# def secret_data_api(api_key: str = Depends(check_api_key)):
#     """
#     This secret API is just for testing. Need access token to access this API.
#     """
#     token = credentials.credentials
#     if (auth_handler.decode_token(token)):
#         return 'Top Secret data only authorized users can access this info'


# @app.get('/not-secret')
# def not_secret_data_api():
#     """
#     This not-secret API is just for testing.
#     """
#     return 'Not secret data'

# Define a route and apply the check_api_key dependency
@app.get("/secure-endpoint/")
async def secure_endpoint(api_key: str = Depends(check_api_key)):
    return {"message": "This is a secure endpoint!"}