# from fastapi import FastAPI, Header, status
# from fastapi import FastAPI
# from src.books.routes import book_router

# version = 'v1'

# app = FastAPI(
#     title='Bookly',
#     description='A RESTful API for a book review web service',
#     version=version,
#     )
    

# app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])



# # @app.get('/greet/{username}')
# # async def greet(username:str):
# #    return {"message":f"Hello {username}"}

# @app.get('/greet/')
# async def greet(username:Optional[str]="User"):
#    return {"message":f"Hello {username}"}



# user_list = [
#    "Jerry",
#    "Joey",
#    "Phil"
# ]

# @app.get('/search')
# async def search_for_user(username:str):
#    for user in user_list:
#     if username in user_list :
#         return {"message":f"details for user {username}"}

#     else:
#         return {"message":"User Not Found"}
    


# # the User model
# class UserSchema(BaseModel):
#    username:str
#    email:str


# users=[]
# @app.post("/create_user")
# async def create_user(user_data:UserSchema):
#    new_user = {
#       "username" : user_data.username,
#       "email": user_data.email
#    }

#    users.append(new_user)

#    return {"message":"User Created successfully","user":new_user}



# @app.get('/get_headers')
# async def get_all_request_headers(
#     user_agent: Optional[str] = Header(None),
#     accept_encoding: Optional[str] = Header(None),
#     referer: Optional[str] = Header(None),
#     connection: Optional[str] = Header(None),
#     accept_language: Optional[str] = Header(None),
#     host: Optional[str] = Header(None),
# ):
#     request_headers = {}
#     request_headers["User-Agent"] = user_agent
#     request_headers["Accept-Encoding"] = accept_encoding
#     request_headers["Referer"] = referer
#     request_headers["Accept-Language"] = accept_language
#     request_headers["Connection"] = connection
#     request_headers["Host"] = host

#     return request_headers





