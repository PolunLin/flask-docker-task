# Gogolook Coding Exercise

## About

* Implement a Restful task list API as well as run this application in container.
* Project status: working
* enviroment: python==3.9, flask==2.0.3
* Database:sqlite3, flask_sqlalchemy
## Table of contents
- [Gogolook Coding Exercise](#gogolook-coding-exercise)
  - [About](#about)
  - [Table of contents](#table-of-contents)
  - [Repository struct](#repository-struct)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Result](#result)

## Repository struct
```bash
.
├── Dockerfile                      // create docker container
├── README.md
├── app                             // main application,database and setting
│   ├── __init__.py
│   └── config
│       ├── config.py               // application config
│       ├── development.db
│       └── test.db                 // database for test
├── manage.py                       // application start entry       
├── requirements.txt
├── task                            // task application
│   ├── models
│   │   └── task.py
│   └── views.py
└── unit_test.py                    // test file
```
## Installation

```bash

pip install -r requirments.txt

```

## Usage

1. You can execute it by run 

    ```bash

    python manage.py

    ```

2. Use Dockerfile to create image


    ```bash

    docker image build -t gogolook .
    docker run -d -p 8080:8080 --name flask_app gogolook

    ```

## Result

1.  GET /tasks (list tasks)

    ```bash

    curl -X GET "localhost:8080/tasks"

    ```
    Response
    ```json
    {
        "result": [
            {"id": 1, "name": "name", "status": 0}
        ]
    }
    ```

2.  POST /task  (create task)

    ```bash

    curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"name": "買晚餐"}' \
    "localhost:8080/task"

    ```
    Response
    ```json
    {
        "result": {"name": "買晚餐", "status": 0, "id": 1}
    }
    ```

3. PUT /task/<id> (update task)

    ```bash
    curl -X PUT \
    -H "Content-Type: application/json" \
     -d '{"name": "買早餐", "status": 1}' \
     "localhost:8080/task/1"
    ```
    Response
    ```json
    {
    "result":{
        "name": "買早餐",
        "status": 1,
        "id": 1
    }
    }
    ```

4. DELETE /task/<id> (delete task)

    ```bash
    curl -X DELETE "localhost:8080/task/1" 
    ```

    ```json
    {
    "result": {
        "msg": "Delete id 1 successfully"
    }
    }
    ```
