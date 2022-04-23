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
    docker run -d -p 80:5000 --name flask_app gogolook

    ```
