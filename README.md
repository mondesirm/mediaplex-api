![mediaplex](assets/logo.svg)
<h1 align="center">BACKEND</h1>

> See [full project](https://github.com/mondesirm/mediaplex) or [FRONTEND](https://github.com/mondesirm/mediaplex-app) for more details.

## Stack
- [🐳 Docker](https://docker.com)
- [🐍 FastAPI](https://fastapi.tiangolo.com)

## Local Setup

1. Create a virtual-env

```python
pyenv virtualenv 3.11.0 any_venv_name
pyenv local any_venv_name
```

2. Install dependencies

```python
pip3 install -r requirements.txt
```

3. Run server with one of the following commands

```python
python main.py
```
```python
uvicorn main:app --reload
```

## Deployment
For hosting purpose, this backend application is hosted on [Okteto](https://www.okteto.com/).

## API Reference
#### Login
```
  POST /login/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | email |
| `password` | `string` | password |

#### Sign Up
```
  POST /user/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | username  |
| `password` | `string` | password |
| `email` | `string` | email |

### Get User
```
  GET /user/{id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. your Access Token |


### Add to Favourites
```
  POST /fav/add
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `string` | **Required**. your Access Token |
| `name` | `string` | **Required**. your Access Token |
| `category` | `string` | **Required**. your Access Token |


### Get Favourites

```
  GET /fav/add
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `none` | `none` | **Required**. your Access Token |


### Delete Favourite
```
  DELETE /fav/delete
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `string` | **Required**. your Access Token |
| `name` | `string` | **Required**. your Access Token |
| `category` | `string` | **Required**. your Access Token |