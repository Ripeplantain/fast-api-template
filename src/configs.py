"""
 Provides a way to use operating system-dependent functionality like reading environment variables.
 """
import os

import psycopg2

def database_connection():
    """
    Establishes and returns a connection to the PostgreSQL database.

    This function retrieves database configuration details from environment variables,
    connects to the database using `psycopg2`, and returns a cursor for executing SQL queries.

    Environment Variables:
        DATABASE (str): Name of the PostgreSQL database.
        DATABASE_PWD (str): Password for the database user.
        DATABASE_USER (str): Username for the database.
        DATABASE_HOST (str): Host address of the PostgreSQL server.

    Returns:
        psycopg2.cursor: A cursor object for executing SQL queries.

    Raises:
        psycopg2.Error: If an error occurs during connection establishment.
    """

    database = os.getenv("DATABASE")
    database_pwd = os.getenv("DATABASE_PWD")
    database_user = os.getenv("DATABASE_USER")
    database_host = os.getenv("DATABASE_HOST")

    url = f"postgresql://{database_user}:{database_pwd}@{database_host}/{database}"

    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    return cursor