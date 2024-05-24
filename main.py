from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"Greeting": 'Hello', "Data": 'How are you?'}

@app.get("/user1") #POST User
async def user1():
    return {"User_Created": 'John Doe', "Create_Date": '24-05-2024'}

@app.get("/user_list") #GET User
async def user_list():
    return {"User0": 'John Doe', "User1": 'Alex Connor', "User2": 'Bob Marley', "User3": 'Benjamin Barles'}

@app.get("/user_zero")
async def user_zero():
    return {"User": 'John Doe', "Create_date": 'unknown', "User_id": '000'}

@app.get("/user_one")
async def user_one():
    return{"User": 'Alex Connor', "Create_date": 'unknown', "User_id": '001'}

@app.get("/user_two")
async def user_two():
    return{"User": 'Bob Marley', "Create_date": 'unknown', "User_id": '002'}

@app.get("/user_three")
async def user_three():
    return{"User": 'Benjamin Barles', "Create_date": 'unknown', "User_id": '003'}

@app.get("/user_id") #GET user_id
async def user_id():
    return{"User_id": '000, 001, 002, 003'}

@app.get("/username") #PUT Username
async def username():
    return{"UpdatedUsername": 'James Franklin', "User_id": '003'}

@app.put("/users")
async def newuser():
    return{"CreatedName": "Marvin", "date": 'unknown'}