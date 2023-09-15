# import os
from flask import Flask, redirect, render_template, request, url_for, jsonify
import psycopg2

# Postgres DB Setup
PostgresPassword = os.getenv('PostgresPassword', 'default_value')
PostgresHost = os.getenv('PostgresHost', 'default_value')


# PostgresDB = 'postgres'
app = Flask(__name__)

app.config['POSTGRES_HOST'] = PostgresHost
app.config['POSTGRES_PORT'] = '5432'
app.config['POSTGRES_DB'] = 'postgres'
app.config['POSTGRES_USER'] = 'postgres'
app.config['POSTGRES_PASSWORD'] = PostgresPassword

# Establish a connection to the Postgres DB 
def connect_to_db():
    conn = psycopg2.connect(
        host=app.config['POSTGRES_HOST'],
        port=app.config['POSTGRES_PORT'],
        database=app.config['POSTGRES_DB'],
        user=app.config['POSTGRES_USER'],
        password=app.config['POSTGRES_PASSWORD']
    )
    return conn

@app.route('/')
def index():  
    return 'Hello from Flask!'

# Read

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):

    # Query the database to retrieve a person with the given ID
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM my_table WHERE id = %s", (user_id,))

    # Fetch the result
    row = cursor.fetchone()
    conn.close()
    if row:
        # Convert the result to a dictionary for JSON serialization
        result = {
            'id': row[0],
            'name': row[1],
            'value': row[2]
        }
        return jsonify(result), 200
    else:
        return jsonify({'message': 'Person not found'}), 404


# Create
@app.route('/api', methods=['POST'])
def create_person():
    # Parse the JSON data from the request
    data = request.get_json()

    # # Validate the input data
    if 'name' not in data or 'value' not in data:
        return jsonify({'message': 'name, and value are required i.e. name: John Doe and value: HNG CEO '}), 400

    # Create a new Person object
    person_name  = data['name']
    person_value  = data['value']

    # Store name and value in the DB
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO my_table (name, value) VALUES('{person_name}', '{person_value}') ; ")

    conn.commit() # Used after Insert to persist the insert query.
    conn.close()
    print(data)

    return jsonify({'message': 'Person created successfully', 
                    "Data":data})


# Update
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):

    # Parse the JSON data from the request
    data = request.get_json()
    updated_name  = data['name']
    updated_value  = data['value']
    
    # Query the database to retrieve a person with the given ID
    conn = connect_to_db()
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM my_table WHERE id = %s", (user_id,))

    cursor.execute(
                "UPDATE my_table SET name = %s, value = %s WHERE id = %s",
                (updated_name, updated_value, user_id)
            )

    conn.commit() # Used to persist the insert query.
    conn.close()
    return jsonify({'message': 'Person updated successfully', 
                    "Data":data})

# Delete
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    try:
        # Query the database to retrieve a person with the given ID
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM my_table WHERE id = %s", (user_id,))

        conn.commit()  # Used to persist the delete query.
        conn.close()

        return jsonify({'message': f'Person with id {user_id} deleted successfully'}), 200
    except Exception as e:
        # Handle any exceptions here
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
