from task.views import init_task
from app import create_app, db
app = create_app("development")

init_task(app)

if __name__=="__main__":
    app.config['JSON_AS_ASCII'] = False # chinese issue
    app.run(host="0.0.0.0", port=5000, debug = True)