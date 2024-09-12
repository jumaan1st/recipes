### API Report: Recipe Management System

#### Overview

The Recipe Management API is a RESTful web service built using Django REST Framework, designed to manage cuisines and recipes. The API includes endpoints for user registration, and authentication for cuisines and recipes.

---

### **1. API Endpoints**

#### **1.1 User Registration and Authentication**

- **Register User**
  - **URL:** `/register/`
  - **Method:** `POST`
  - **Description:** Creates a new user and returns an authentication token.
  - **Request Body (JSON):**
    ```json
    {
        "username": "newuser",
        "password": "yourpassword",
        "email": "user@example.com"
    }
    ```
  - **Response:**
    ```json
    {
        "token": "generated_token_here"
    }
    ```

- **Login User**
  - **URL:** `/login/`
  - **Method:** `POST`
  - **Description:** Authenticates a user and returns an authentication token.
  - **Request Body (JSON):**
    ```json
    {
        "username": "newuser",
        "password": "yourpassword"
    }
    ```
  - **Response:**
    ```json
    {
        "token": "generated_token_here"
    }
    ```

#### **1.2 Cuisines Endpoints**

- **List Cuisines**
  - **URL:** `/cuisines/`
  - **Method:** `GET`
  - **Description:** Retrieves a list of all cuisines.
  - **Headers:** 
    ```
    Authorization: Token <your_token_here>
    ```
  - **Response:**
    ```json
    [
        {
            "id": 1,
            "name": "Indian",
            "recipes": [
                {
                    "id": 1,
                    "title": "Butter Chicken",
                    "description": "A classic Indian dish."
                }
            ]
        },
        {
            "id": 2,
            "name": "Italian",
            "recipes": []
        }
    ]
    ```

- **View Specific Cuisine**
  - **URL:** `/cuisines/{id}/`
  - **Method:** `GET`
  - **Description:** Retrieves details of a specific cuisine.
  - **Headers:** 
    ```
    Authorization: Token <your_token_here>
    ```
  - **Response:**
    ```json
    {
        "id": 1,
        "name": "Indian",
        "recipes": [
            {
                "id": 1,
                "title": "Butter Chicken",
                "description": "A classic Indian dish."
            }
        ]
    }
    ```

#### **1.3 Recipes Endpoints**

- **List Recipes**
  - **URL:** `/recipes/`
  - **Method:** `GET`
  - **Description:** Retrieves a list of all recipes.
  - **Headers:** 
    ```
    Authorization: Token <your_token_here>
    ```
  - **Response:**
    ```json
    [
        {
            "id": 1,
            "title": "Butter Chicken",
            "description": "A classic Indian dish.",
            "cuisine": 1
        },
        {
            "id": 2,
            "title": "Pizza",
            "description": "Delicious cheese pizza.",
            "cuisine": 2
        }
    ]
    ```

- **View Specific Recipe**
  - **URL:** `/recipes/{id}/`
  - **Method:** `GET`
  - **Description:** Retrieves details of a specific recipe.
  - **Headers:** 
    ```
    Authorization: Token <your_token_here>
    ```
  - **Response:**
    ```json
    {
        "id": 2,
        "title": "Pizza",
        "description": "Delicious cheese pizza.",
        "cuisine": 2
    }
    ```

- **Create Recipe**
  - **URL:** `/recipes/`
  - **Method:** `POST`
  - **Description:** Adds a new recipe to a cuisine.
  - **Headers:** 
    ```
    Authorization: Token <your_token_here>
    ```
  - **Request Body (JSON):**
    ```json
    {
        "title": "Pizza",
        "description": "Delicious cheese pizza",
        "cuisine": 2
    }
    ```
  - **Response:**
    ```json
    {
        "id": 2,
        "title": "Pizza",
        "description": "Delicious cheese pizza",
        "cuisine": 2
    }
    ```

---

### **2. How the API Works**

#### **2.1 User Registration and Authentication**

1. **User Registration:**
   - A new user sends a `POST` request to `/register/` with their username, password, and email.
   - The server creates a new user entry in the database and generates a token for the user.
   - The token is returned in the response, which the user will use for authenticated requests.

2. **User Login:**
   - An existing user sends a `POST` request to `/login/` with their username and password.
   - The server verifies the credentials and returns an authentication token if valid.

#### **2.2 Token-Based Authentication**

- The API uses token-based authentication to protect endpoints. 
- Users include the token in the `Authorization` header of their requests.
- The server verifies the token before granting access to protected resources.

#### **2.3 Cuisines Management**

- **List Cuisines:** 
  - Users with a valid token can request the list of all cuisines.
- **View Specific Cuisine:**
  - Users can view details of a specific cuisine using its ID.

#### **2.4 Recipes Management**

- **List Recipes:**
  - Users with a valid token can request the list of all recipes.
- **View Specific Recipe:**
  - Users can view details of a specific recipe using its ID.
- **Create Recipe:**
  - Authenticated users can add new recipes to a specified cuisine by providing the recipe details and the cuisine ID.

---

### **3. Error Handling**

- **Authentication Errors:**
  - If a request is made without a valid token, the server responds with an error message:
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```
  - If an invalid token is used, the server responds with:
    ```json
    {
        "detail": "Invalid token."
    }
    ```

- **Resource Not Found:**
  - If a requested resource (cuisine or recipe) is not found, the server responds with:
    ```json
    {
        "detail": "Not found."
    }
    ```

- **Validation Errors:**
  - If there are validation issues with the request data (e.g., missing fields), the server responds with:
    ```json
    {
        "field_name": ["Error message"]
    }
    ```

---

### **4. Summary**

The Recipe Management API allows users to manage cuisines and recipes with secure, token-based authentication. Users can register and log in to obtain tokens that are used to access and modify data related to cuisines and recipes. The API provides endpoints for listing, viewing, and creating recipes, with detailed error handling to guide users through proper usage and troubleshoot issues.

Feel free to ask if you need more information or have any specific questions about the API!
