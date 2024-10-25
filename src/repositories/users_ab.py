from abc import ABC, abstractmethod
from src.dtos.write.users import UsersWrite

class UsersRepositoryAbstruct(ABC):
    """
    An abstract base class for managing user data in a repository. This class defines 
    the basic operations for adding, deleting, updating, and retrieving users.

    Methods:
        add_user(user: UsersWrite, userid: str):
            Adds a new user with the provided user data and ID. Must be implemented by a subclass.

        delete_user(userid: str):
            Deletes an existing user with the given ID. Must be implemented by a subclass.

        update_user(userid: str, user: UsersWrite):
            Updates the user information with the given ID. Must be implemented by a subclass.

        get_user_by_id(userid: str) -> any:
            Retrieves user information for the specified ID. Must be implemented by a subclass.

        get_all_user() -> any:
            Retrieves all user records. Must be implemented by a subclass.
    """

    @staticmethod
    @abstractmethod
    def add_user(user: UsersWrite, userid: str) -> None:
        """
        Adds a new user with the provided user data and ID.

        Args:
            user (UsersWrite): An object containing the user's information to be added.
            id (str): The ID associated with the user to be added.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        raise NotImplementedError()
    
    @staticmethod
    @abstractmethod
    def delete_user(userid: str) -> None:
        """
        Delete an existsing user

        Args:
            userid (str): The ID associated with the user to be deleted.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        raise NotImplementedError()
    
    @staticmethod
    @abstractmethod
    def update_user(userid: str, user: UsersWrite) -> None:
        """
        Updates the user information for the given ID.

        Args:
            userid (str): The ID of the user to be updated.
            user (UsersWrite): An object containing the updated user information.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        raise NotImplementedError()
    
    @staticmethod
    @abstractmethod
    def get_user_by_id(userid) -> any:
        """
        Retrieves the user information for the specified ID.

        Args:
            userid (str): The ID of the user to retrieve.

        Returns:
            any: The retrieved user information. The return type can vary depending on the implementation.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        raise NotImplementedError()
    
    @staticmethod
    @abstractmethod
    def get_all_user() -> any:
        """
        Retrieves all user records.

        Returns:
            any: A list or collection of all users. The return type can vary depending on the implementation.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        raise NotImplementedError()