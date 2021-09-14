from os import name
from re import X
from flask import Flask, request, jsonify
from models import user, task  # call model file
from flask_cors import CORS  # to avoid cors error in different frontend like react js or any other
from bson import ObjectId
from types import SimpleNamespace
import json


app = Flask(__name__)
CORS(app)

user=user.User()
task= task.Task() 

@app.route('/', methods=['GET'])
def test():
    if request.method == "GET":
        return jsonify({"response":"working"})

#user get request
@app.route('/users/', methods=['GET'])
def get_users():
    return jsonify(user.find({})), 200

#user post request
@app.route('/users/', methods=['POST'])
def add_users():
    if request.method == "POST":
        name = request.json["name"]
        print(name)
        response = user.create({'name': name})
        return response, 201

#user put request
@app.route('/users/<string:user_id>/', methods=['PUT'])
def update_users(user_id):
    if request.method == "PUT":
        name = request.json['name']
        response = user.update(user_id, {'name': name})
        return response, 201

#user delete request
@app.route('/users/<string:user_id>/', methods=['DELETE'])
def delete_users(user_id):
    if request.method == "DELETE":
        user.delete(user_id)
        x =task.find({'owner':user_id})
        for i in x :
            task.delete(i['_id'])
        return "Record Deleted"




#task get request
@app.route('/task/', methods=['GET'])
def get_tasks():
    return jsonify(task.find({})), 200

#task post request
@app.route('/task/', methods=['POST'])
def add_tasks():
    if request.method == "POST":
        taskName = request.json["taskName"]
        owner= request.json["owner"]
        response = task.create({'taskName': taskName, 'owner':owner })
        return response, 201

#task put request
@app.route('/task/<string:task_id>/', methods=['PUT'])
def update_tasks(task_id):
    if request.method == "PUT":
        taskName = request.json['taskName']
        response = task.update(task_id, {'taskName': taskName})
        return response, 201


#task delete request
@app.route('/task/<string:task_id>/', methods=['DELETE'])
def delete_tasks(task_id):
    if request.method == "DELETE":
        task.delete(task_id)
        return "Record Deleted"

#task get request by user specific
@app.route('/task/user/<string:user_id>/',methods=['GET'])
def get_task_by_user(user_id):
    return jsonify(task.find({"owner":user_id})), 200



if __name__ == '__main__':
    app.run(debug=True)