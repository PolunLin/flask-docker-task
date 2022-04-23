from unittest import result
from flask import Flask, jsonify, request,Response
from flask_sqlalchemy import SQLAlchemy
from task.models.task import Task,db

def init_task(app):
    # GET /tasks (list tasks)
    @app.route("/tasks", methods = ["GET"])
    def show_task():
        context ={}
        tasks_list = Task.query.order_by(Task.id).all()
        context['result'] = [task.to_dict() for task in tasks_list]
        return context,200

    # POST /task  (create task)
    @app.route("/task", methods = ["POST"])
    def create_task():
        request_data = request.get_json() # get the request data
        context ={}
        if 'name' not in request_data:
            msg ={'msg':'Bad request: "name" is not in reqeust data'}
            context['result'] = msg
            return context,400  #  Bad request
        else:
            status = request_data.get("status",0)
            name = request_data.get("name",None)
            if name ==None or len(str(name))==0:
                msg = {"msg":"Error Input: 'name' should not be empty."}
                context['result'] = msg
                return context,400
            if status !=0 and status !=1:
                msg = {"msg":"Error Input: 'status' is invalid data format."}
                context['result'] = msg
                return context,400
            try:
                task_data = Task(name = request_data["name"], status = status)
                db.session.add(task_data)
                db.session.commit()
                context['result'] = task_data.to_dict()
                return context,201
            except:
                db.session.rollback()
                raise
            
    
    # PUT /task/<id> (update task)
    @app.route("/task/<int:id>", methods = ["PUT"])
    def update_task(id):
        context = {}
        request_data = request.get_json() # get the request data
        if 'name' not in request_data or 'status' not in request_data: ## 
            msg = {"msg":"Error Input: 'name' or  'status' is not in reqeust data."}
            context['result'] = msg
            return context,400
        name = request_data.get("name",None)
        status = request_data.get("status",None)
        if status !=0 and status !=1:
            msg = {"msg":"Error Input: 'status' is invalid data format."}
            context['result'] = msg
            return context,400
        if name ==None or len(str(name))==0:
            msg = {"msg":"Error Input: 'name' should not be empty."}
            context['result'] = msg
            return context,400
        try:
            updated_data = Task.query.filter_by(id=id).first()
            
            if  updated_data ==None :
                msg =  {"msg":"Error Index: Can't find this record."}
                context['result'] =msg
                return context,404
            updated_data.name = str(name)
            
            updated_data.status = status
            
            db.session.commit()
            context['result'] = updated_data.to_dict()
            return context,201
        except:
            db.session.rollback()
            raise
        
        
    # DELETE /task/<id> (delete task)
    @app.route("/task/<int:id>", methods = ["DELETE"])
    def delete_task(id):
        context = {}
        try:
            deleted_task = Task.query.filter_by(id=id).first()
            if not deleted_task:
                context['result'] = [{"msg":"Error Input: Can't find this record."}]
                return context, 404
            else:
                db.session.delete(deleted_task)
                db.session.commit()
                context['result'] = [{"msg":f"Delete id {id} successfully"}]
                return context, 200
        except:
            db.session.rollback()
            raise