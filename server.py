from sanic import Sanic
from sanic.response import json
from connection import session
from models import User
from connection import Base, engine

app = Sanic("MyApp")

Base.metadata.create_all(engine)
@app.route("/")
async def home(request):
    return json({"message": "Welcome to the backend!"})

@app.route("/healthcheck")
async def healthcheck(request):
    return json({"status": "ok"})

@app.route("/users", methods=["GET"], name="get_users")
async def get_users(request):
    users = session.query(User).all()
    session.close()

    return json({"users": [{"id": user.id, "name": user.name, "email": user.email} for user in users]})

@app.route("/users", methods=["POST"], name="create_user")  
async def create_user(request):
    body = request.json
    user_data = {
        "name": body.get("name"),
        "email": body.get("email"),
        "phone_number": body.get("phone_number"),
        "designation": body.get("designation"),
        "department": body.get("department"),
    }
    user = User(user_data)
    session.add(user)
    return json({"user": {"id": user.id, "name": user.name, "email": user.email}})

# @app.route("/users/<id>", methods=["GET"], name="get_user_by_id")
