# HNGx STAGE 2 API Documentation

## Table of Contents

- [Introduction](#introduction)
- [API Endpoints](#api-endpoints)
  - [1. Create a New Person](#1-create-a-new-person)
  - [2. Retrieve a Person](#2-retrieve-a-person)
  - [3. Update a Person](#3-update-a-person)
  - [4. Delete a Person](#4-delete-a-person)
- [Sample Usage](#sample-usage)
- [Known Limitations and Assumptions](#known-limitations-and-assumptions)
- [Setup and Deployment](#setup-and-deployment)
  - [Local Development](#local-development)
  - [Server Deployment](#server-deployment)

## Introduction

This API allows you to manage a collection of persons. You can create, retrieve, update, and delete persons using the provided endpoints.

## API Endpoints

### 1. Create a New Person

- **Endpoint:** `/api/`
- **HTTP Method:** POST

#### POST Request Format

- **Postman and Search Engine Format:**
  - URL: `https://hng-stage-two-fek8.onrender.com/api/`
  - Headers:
    - Content-Type: application/json
  - Body (JSON):

    ```json
    {
      "name": "Hutty"
    }
    ```

#### POST Response Format

- **Successful Response (HTTP 201 Created):**

  ```json
  {
    "id": 1,
    "name": "Hutty"
  }
  ```

- **Error Response (HTTP 400 Bad Request):**

  ```json
  {
    "error": ["Name must be a string"]
  }
  ```

### 2. Retrieve a Person

- **Endpoint:** `/api/<str:pk>`
- **HTTP Method:** GET

#### GET Request Format

- **Postman and Search Engine Format:**
  - URL: `https://hng-stage-two-fek8.onrender.com/api/1` (where `1` is the person's ID)
  OR
  - URL: `https://hng-stage-two-fek8.onrender.com/api/hutty` (where `hutty` is the person's name)

#### GET Response Format

- **Successful Response (HTTP 200 OK):**

  ```json
  {
    "id": 1,
    "name": "Hutty"
  }
  ```

- **Error Response (HTTP 404 Not Found):**

  ```json
  {
    "error": "User does not exist."
  }
  ```

### 3. Update a Person

- **Endpoint:** `/api/<str:pk>`
- **HTTP Method:** PUT

#### PUT Request Format

- **Postman and Search Engine Format:**
  - URL: `https://hng-stage-two-fek8.onrender.com/api/1` (where `1` is the person's ID)
  - Headers:
    - Content-Type: application/json
  - Body (JSON):

    ```json
    {
      "name": "Henry"
    }
    ```

#### PUT Response Format

- **Successful Response (HTTP 202 Accepted):**

  ```json
  {
    "id": 1,
    "name": "Henry"
  }
  ```

- **Error Response (HTTP 400 Bad Request or HTTP 404 Not Found):**

  ```json
  {
    "error": "User does not exist." 
    OR
    "error": "Name must be a string"
  }
  ```

### 4. Delete a Person

- **Endpoint:** `/api/<int:pk>`
- **HTTP Method:** DELETE

#### DELETE Request Format

- **Postman and Search Engine Format:**
  - URL: `https://hng-stage-two-fek8.onrender.com/api/1` (where `1` is the person's ID)

#### DELETE Response Format

- **Successful Response (HTTP 204 No Content):**
  - No response body.

## Sample Usage

Below are examples of how to use the API with different endpoints, including requests and expected responses.

**Create a New Person (POST):**

```json
Request:
POST https://hng-stage-two-fek8.onrender.com/api/
Headers: Content-Type: application/json
Body (JSON):
{
  "name": "Hutty"
}

Response (HTTP 201 Created):
{
  "id": 1,
  "name": "Hutty"
}
```

**Retrieve a Person (GET):**

```json
Request:
GET https://hng-stage-two-fek8.onrender.com/api/1

Response (HTTP 200 OK):
{
  "id": 1,
  "name": "Hutty"
}
```

**Update a Person (PUT):**

```json
Request:
PUT https://hng-stage-two-fek8.onrender.com/api/1


Headers: Content-Type: application/json
Body (JSON):
{
  "name": "Henry Hart"
}

Response (HTTP 202 Accepted):
{
  "id": 1
  "name": "New Name"
}
```

**Delete a Person (DELETE):**

```json
Request:
DELETE https://hng-stage-two-fek8.onrender.com/api/1

Response (HTTP 204 No Content):
No response body.
```

## Known Limitations and Assumptions

The API assumes that each person has a unique name.
No authentication or authorization mechanisms are implemented in this version of the API.

## Setup and Deployment

### Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/Hutty10/stage_two.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Your API should now be accessible at `http://localhost:8000/api/`.

### Server Deployment
