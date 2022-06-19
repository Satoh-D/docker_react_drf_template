# docker_react_drf_template

React, Django REST Framework（DRF）を使うためのDockerコンテナ群

# Installations

```bash
$ git pull [repo]
$ cd [repo]
$ docker-compose up -d
```

# Start Django

```bash
$ docker exec -ti works_backend bash

# logged in django container
$ chmod 700 start_server.sh
$ ./start_server.sh
# access on browser http://localhost:8000
```

# Start React

```bash
$ docker exec -ti works_frontend bash

# logged in react container
$ npm ci
$ npm start
# access on browser http://localhost:3000
```

## Features

- `gunicorn`の設定追加
- `Nginxコンテナ`の追加
    - React, DRFへのリバースプロキシ設定
