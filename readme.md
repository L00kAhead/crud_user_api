# User Management API
- This documentation provides an overview and usage details for the FastAPI User Management API. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on user data. It includes endpoints to fetch users, add a new user, update an existing user, and delete a user.

## Requirements
To run this API, you need the following dependencies installed:
- Python 3.7 or above
- FastAPI
- uvicorn
- pydantic  

**Clone the project and run:**
```
pip install -r requirements.txt
```
Check the `requirements.txt` to see the complete list of dependencies.

## API Endpoints

### Hello Endpoint
**`URL: /`**

- Method: GET
- Description: This endpoint returns a simple greeting message.

**Response**:
- HTTP Status Code: 200 (OK)
- Body: json
```
{
    "msg": "Hello There!"
}
```

### Fetch Users Endpoint
**`URL: /api/v1/users/`**

- Method: GET
- Description: This endpoint retrieves a list of all users.

**Response:**
- HTTP Status Code: 200 (OK)
- Body: List of User objects

### Add User Endpoint
**`URL: /api/v1/users`**

- Method: POST
- Description: This endpoint adds a new user to the database.

**Request Body:**
User (JSON object)
- id (optional): UUID (Universally Unique Identifier) of the user. If not provided, it will be generated automatically.
- first_name (required): First name of the user.
- middle_name (optional): Middle name of the user.
- last_name (required): Last name of the user.
- gender (required): Gender of the user. It should be one of the values: "male" or "female".
- roles (required): List of roles assigned to the user. Each role should be one of the values: "admin", "user", or "student".

**Response:**
- HTTP Status Code: 200 (OK)
- Body:json
```
{
    "id": "<generated_user_id>"
}
```

### Update User Endpoint
`URL: /api/v1/users/{user_id}`
- Method: PUT
- Description: This endpoint updates an existing user's information.

**Path Parameters:**
- user_id (UUID): The ID of the user to be updated.

**Request Body:**
UserUpdateRequest (JSON object)
- first_name (optional): Updated first name of the user.
- middle_name (optional): Updated middle name of the user.
- last_name (optional): Updated last name of the user.
- gender (optional): Updated gender of the user. It should be one of the values: "male" or "female".
- roles (optional): Updated list of roles assigned to the user. Each role should be one of the values: "admin", "user", or "student".

**Response:**
- HTTP Status Code: 200 (OK)

### Delete User Endpoint
`URL: /api/v1/users/{user_id}`

- Method: DELETE
- Description: This endpoint deletes an existing user.

**Path Parameters:**
- user_id (UUID): The ID of the user to be deleted.

**Response:**
- HTTP Status Code: 200 (OK)

## Data Models
- Gender Enum : The Gender enum represents the possible gender values for a user.
    - male: Male gender
    - female: Female gender
- Role Enum : The Role enum represents the possible roles that can be assigned to a user.
    - admin: Administrator role
    - user: Regular user role
    - student: Student role

### User Model
The User model represents a user object with the following attributes:

- id (UUID, optional): Universally Unique Identifier of the user.
- first_name (str, required): First name of the user.
- middle_name (str, optional): Middle name of the user.
- last_name (str, required): Last name of the user.
- gender (Gender, required): Gender of the user.
- roles (List[Role], required): List of roles assigned to the user.

### UserUpdateRequest Model
The UserUpdateRequest model represents the fields that can be updated for a user.

- first_name (str, optional): Updated first name of the user.
- middle_name (str, optional): Updated middle name of the user.
- last_name (str, optional): Updated last name of the user.
- gender (Gender, optional): Updated gender of the user.
- roles (List[Role], optional): Updated list of roles assigned to the user.

## Example Usage

### Fetch all users:

GET /api/v1/users/

### Add a new user:

POST /api/v1/users
Body:
```
{
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "roles": ["user"]
}
```

### Update an existing user:

`PUT /api/v1/users/{user_id}`
Body:
```
{
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "roles": ["admin", "user"]
}

```

### Delete a user:

`DELETE /api/v1/users/{user_id}`


## Swagger Documentation
FastAPI provides automatic documentation through Swagger UI. You can access the Swagger documentation by visiting the /docs endpoint in your browser when the API is running. For example, if you are running the API locally, you can access the Swagger documentation at **http://localhost:8000/docs'**.