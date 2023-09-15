# REST API Documentation

Documentation for a simple Flask REST API. This API provides CRUD (Create, Read, Update, Delete) operations on a "person" resource, interfacing with a PostgreSQL database. 

## Table of Contents

- [Endpoints](#endpoints)
- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
- [Request/Response Formats](#requestresponse-formats)

## Endpoints

### Create (POST)

- **Endpoint:** `/api`
- **HTTP Method:** POST
- **Description:** Create a new person resource.
- **Request Body:** JSON object containing "name" and "value" fields.
- **Example:**
  ```json
  {
    "name": "John Doe",
    "value": "HNG CEO"
  }

Response: JSON response with a success message.

### Read (GET)

- **Endpoint:** `/api/<int:user_id>`
- **HTTP Method:** GET
- **Description:** Retrieve details of a person resource by id.
- **Response:** JSON response with person details if found, or a "Person not found" message.

### Update (PUT)

- **Endpoint:** `/api/<int:user_id>`
- **HTTP Method:** PUT
- **Description:** Modify details of an existing person resource by id.
- **Request Body:** JSON object containing updated "name" and "value" fields.
- **Example:**
  ```json
  {
    "name": "Updated Name",
    "value": "Updated Value"
  }
Response: JSON response with a success message.


### Delete (DELETE)

- **Endpoint:** `/api/<int:user_id>`
- **HTTP Method:** DELETE
- **Description:** Remove a person resource by id.
- **Response:** JSON response with a success message if the deletion is successful.

### Setup Instructions

1. Clone this GitHub repository to your local machine.
2. Ensure you have Python and Flask installed.
3. Install the required packages using `pip install -r requirements.txt`.
4. Configure the PostgreSQL database details in the Flask app (`app.config` section).
5. Run the Flask app using `python app.py`.

### API Usage

You can use this API by sending HTTP requests to the provided endpoints. You can use tools like curl, Postman, or any programming language's HTTP library to interact with the API.
