# API Documentation

## Menu Items

- **GET** `/api/menu-items/`

  - **Description**: Retrieve a list of all menu items.
  - **Authorization**: Token required.

- **GET** `/api/menu-items/<int:id_menu>/`
  - **Description**: Retrieve detailed information about a specific menu item identified by `id_menu`.
  - **Parameters**:
    - `id_menu`: The unique identifier of the menu item.
  - **Authorization**: Token required.

## Reservations

- **GET** `/api/tables/`
  - **Description**: Retrieve a list of all reservations.
  - **Authorization**: Token required.

## Authentication

- **POST** `/auth/token/login/`

  - **Description**: Authenticate a user and obtain an authentication token.
  - **Body**:
    - `username`: The username of the user.
    - `password`: The password of the user.
  - **Authorization**: None.

- **POST** `/auth/users/`

  - **Description**: Register a new user.
  - **Body**:
    - `username`: The username for the new user.
    - `password`: The password for the new user.
    - `email`: The email address of the new user.
  - **Authorization**: None.

- **POST** `/auth/token/logout/`
  - **Description**: Log out the user by deleting the authentication token.
  - **Authorization**: Token required.

## Authentication Token Usage

To access endpoints that require authentication, include the token in the request header:

- **Header**:
  - `Authorization`: `Token <your_token_here>`

## Example Requests

**Getting Menu Items:**

```http
GET /api/menu-items/
```
