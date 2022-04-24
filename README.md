# Gogolook Coding Exercise

## About

* Use flask and docker to create a service that can manage tasks.
* Project status: working

## Table of contents

>   * [Gogolook Coding Exercise](https://github.com/PolunLin/gogolook-exercise)
>   * [About](#about)
>   * [Table of contents](#table-of-contents)
>   * [Installation](#installation)
>   * [Usage](#usage)
>   * [Result](#result)


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


    ```

    docker image build -t gogolook .
    docker run -d -p 8080:8080 --name flask_app gogolook

    ```

## Result

1.  GET /tasks (list tasks)

    ```

    curl -X GET "localhost:8080/tasks"

    ```
    Response
    ```
    {
        "result": [
            {"id": 1, "name": "name", "status": 0}
        ]
    }
    ```

2.  POST /task  (create task)

    ```

    curl -X POST -H "Content-Type: application/json" -d '{"name": "買晚餐, "status": 0}' "localhost:8080/task"

    ```
    Response
    ```
    {
        "result": {"name": "買晚餐", "status": 0, "id": 1}
    }
    ```

3. PUT /task/<id> (update task)

    ```
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "買早餐", "status": 1}' "localhost:8080/task/1"
    ```
    Response
    ```
    {
    "result":{
        "name": "買早餐",
        "status": 1,
        "id": 1
    }
    }
    ```

4. DELETE /task/<id> (delete task)

    ```
    curl -X DELETE "localhost/task/1" 
    ```
    
    response status code 200