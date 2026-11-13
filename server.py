from flask import Flask, request

app = Flask(__name__)

users = []

print(app)

@app.get("/")
def home_page():
    return "Hello, server!"


@app.get("/names")
def names():
    return {
        "response": ["John", "Alex", "Kira"]
    }

@app.get("/names/add")
def add_name():
    data = request.get_json()
    name = data.get("name")
    users.append(name)
    return {
        
    }
app.run()