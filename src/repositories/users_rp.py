from src.repositories.users_ab import UsersRepositoryAbstruct
from src.dtos.write.users import UsersWrite
from src.configs import database_connection

class UsersRepository(UsersRepositoryAbstruct):
    """
    Concrete implementation of the UsersRepositoryAbstruct for managing user data in the database.
    This class provides static methods to add, delete, update, and retrieve user information 
    using raw SQL queries with a PostgreSQL database.

    Methods:
        add_user(user: UsersWrite, userid: str):
            Adds a new user with the provided user data and ID.
        
        delete_user(userid: str):
            Deletes an existing user with the given ID.
        
        update_user(userid: str, user: UsersWrite):
            Updates the user information for the given ID.
        
        get_user_by_id(userid: str) -> any:
            Retrieves user information for the specified ID.
        
        get_all_user() -> any:
            Retrieves all user records from the database.
    """

    @staticmethod
    def add_user(user: UsersWrite, userid: str) -> None:
        """
        Adds a new user with the provided user data and ID to the database.

        Args:
            user (UsersWrite): An object containing the user's information to be added.
            userid (str): The ID associated with the user to be added.
        """
        cursor = database_connection()
        query = "INSERT INTO users(id, fullname, age, email, location) VALUES(%s, %s, %s, %s, %s)"
        cursor.execute(query, (userid, user.fullname, user.age, user.email, user.location,))

        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def delete_user(userid: str) -> None:
        """
        Deletes an existing user with the given ID from the database.

        Args:
            userid (str): The ID associated with the user to be deleted.
        """
        cursor = database_connection()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (userid,))

        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def update_user(userid: str, user: UsersWrite) -> None:
        """
        Updates the user information for the given ID in the database.

        Args:
            userid (str): The ID of the user to be updated.
            user (UsersWrite): An object containing the user's updated information.
        """
        cursor = database_connection()
        query = "UPDATE users SET fullname=%s, age=%s, email=%s, location=%s WHERE id=%s"

        cursor.execute(query, (user.fullname, user.age, user.email, user.location, userid,))
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def get_user_by_id(userid: str) -> any:
        """
        Retrieves the user information for the specified ID from the database.

        Args:
            userid (str): The ID of the user to retrieve.

        Returns:
            any: A tuple containing the user's information (id, fullname, age, email, location) 
            if found, otherwise None.
        """
        cursor = database_connection()
        query = "SELECT id, fullname, age, email, location FROM users WHERE id = %s"
        cursor.execute(query, (userid,))
        response = cursor.fetchone()

        cursor.close()
        return response

    @staticmethod
    def get_all_user() -> any:
        """
        Retrieves all user records from the database.

        Returns:
            any: A list of tuples containing user information (id, fullname, age, email, location) 
            for each user in the database.
        """
        cursor = database_connection()
        query = "SELECT id, fullname, age, email, location FROM users"
        cursor.execute(query)
        response = cursor.fetchall()

        cursor.close()
        return response