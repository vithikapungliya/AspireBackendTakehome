import psycopg2
from psycopg2 import sql
import os

def make_conection():
    """
    Connect to a PostgreSQL database and return the connection object.
    """
    try:
        DATABASE_URL= os.getenv("DATABASE1_URL")
        connection = psycopg2.connect(DATABASE_URL)
        print("Connection to PostgreSQL database successful.")
        return connection
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None

# def make_conection():
#     global connection
#     HOST = "localhost"
#     DATABASE = os.getenv("POSTGRES_DB")
#     USER = os.getenv("POSTGRES_USER")
#     PASSWORD = os.getenv("POSTGRES_PASSWORD")
#     PORT = 15432  # Default PostgreSQL port
    
#     connection = connect_to_postgresql(HOST, DATABASE, USER, PASSWORD, PORT)
#     return connection
    


# from fastapi import Request

# def get_connection(request: Request):
#     return request.app.state.connection