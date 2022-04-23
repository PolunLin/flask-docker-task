import unittest
import json
from task.views import init_task
from app import create_app, db,Task
class TestRoute(unittest.TestCase):
    def setUp(self):
        self.app = create_app("unittest")
        init_task(self.app)
        self.client = self.app.test_client()
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
        
        test_data = Task("test_data", 0)
        with self.app.app_context():
            db.session.add(test_data)
            db.session.commit()
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    # test GET /tasks (list tasks)
    def test_show_tasks(self):
        response = self.client.get("/tasks")
        self.assertEqual(json.loads(response.data)['result'],[{'id': 1, 'name': 'test_data', 'status': 0}])
        self.assertEqual(response.status_code, 200)

    # test POST /task  (create task)
    def test_create_task(self):
        cases_data = [{'name':'買早餐', 'status':1},                # right case
                      {'name':'買午餐'},                            # right case
                      {'name':'買晚餐', 'status':0},                # right case
                      {'status':0},                                # 400 case
                      {'name':'買晚餐1', 'status':3},               # 400 case
                      {'name':'買晚餐2', 'status':"string"},        # 400 case
                      ]   
        
        # {'name':'買早餐', 'status':1}
        post_data = cases_data[0]
        response = self.client.post("/task",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['result']['name'], post_data['name'])
        self.assertEqual(json.loads(response.data)['result']['status'], post_data['status'])

        # {'name':'買午餐'}
        post_data = cases_data[1]
        response = self.client.post("/task",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['result']['name'], post_data['name'])
        self.assertEqual(json.loads(response.data)['result']['status'], 0)
        
        
        # {'name':'買晚餐', 'status':0}
        post_data = cases_data[2]
        response = self.client.post("/task",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['result']['name'], post_data['name'])
        self.assertEqual(json.loads(response.data)['result']['status'], post_data['status'])

        # {'status':0}
        post_data = cases_data[3]
        response = self.client.post("/task",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 400)

        # {'name':'買晚餐1', 'status':3}
        post_data = cases_data[4]
        response = self.client.post("/task",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 400)

        # {'name':'買晚餐2', 'status':"string"}
        post_data = cases_data[4]
        response = self.client.post("/task",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    
    ## test PUT /task/<id> (update task)
    def test_update_task(self):
        cases_data = [{'id':1,'name':'買早餐', 'status':1},                # right case
                      {'id':1,'name':'買午餐'},                            # 400 case
                      {'id':1,'status':0},                                # 400 case
                      {'id':1,'name':'', 'status':1},                     # 400 case
                      {'id':1,'name':'買午餐', 'status':3},                # 400 case
                      {'id':2,'name':'買晚餐', 'status':1},                # 404 case
                      ]   
        # {'id':0,'name':'買早餐', 'status':1}
        post_data = cases_data[0]
        response = self.client.put("/task/1",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['result']['name'], post_data['name'])
        self.assertEqual(json.loads(response.data)['result']['status'], post_data['status'])

        # {'name':'買午餐'}
        post_data = cases_data[1]
        response = self.client.put("/task/1",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 400)

        # {'name':'買晚餐', 'status':0}
        post_data = cases_data[2]
        response = self.client.put("/task/1",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 400)

        # {'status':0}
        post_data = cases_data[3]
        response = self.client.put("/task/1",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 400)

        # {'id':1,'name':"買午餐", 'status':3}, 
        post_data = cases_data[4]
        response = self.client.put("/task/1",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 400)

        # {'id':2,'name':"買午餐", 'status':2}
        post_data = cases_data[5]
        response = self.client.put("/task/2",data=json.dumps(post_data),content_type='application/json')
        self.assertEqual(response.status_code, 404)
    # test DELETE /task/<id>
    def test_delete_task(self):
        res = self.client.delete("/task/1")
        self.assertEqual(res.status_code, 200)

        res = self.client.delete("/task/222")
        self.assertEqual(res.status_code, 404)
    
if __name__ == '__main__':
    unittest.main()