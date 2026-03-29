# from flask import request, jsonify  # type: ignore
 
# def create_user(): 
#     data = request.get_json(force=True, silent=True)
    
#     print("hello: ", data)
#     # if not data:
#     #     return jsonify({"error": "No JSON data provided"}), 200

#     response = jsonify({
#         "message": "create_user hit"
#     })

#     response.headers["X-Custom-Header"] = "MyValue"

#     headers = {"Access-Control-Allow-Origin": "*", "Cache-Control": "no-cache", "Content-Type": "application/json"}

#     return response
# controllers/user_controller.py
from flask import request, jsonify
from models.user_model import User, db

def create_user():
    data = request.get_json()

    user = User(name=data["name"], email=data["email"])
    user.save()
    
    print(data)

    return jsonify({"message": "User created"})