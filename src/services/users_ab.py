"""
Module containing the abstract base class for user service operations.

This module defines an abstract base class, `UsersAbstractService`, which provides
an interface for managing user-related operations such as adding, deleting, updating,
and retrieving user information. Subclasses should implement these methods to interact
with specific services or business logic.
"""

from abc import ABC, abstractmethod

from src.dtos.read.users import UsersRead
from src.dtos.write.users import UsersWrite
from src.dtos.response import Response

class UsersAbstractService(ABC):
    """
    An abstract base class that defines the interface for user-related operations.

    This class serves as a blueprint for any service class that manages user-related operations,
    enforcing the implementation of methods for adding, deleting, updating, and retrieving users.
    """

    @staticmethod
    @abstractmethod
    def add_user(user: UsersWrite) -> Response[UsersRead]:
        """
        Adds a new user.

        Args:
            user (UsersWrite): The data of the user to be added.

        Returns:
            Response[UsersRead]: A response object containing the newly created user's information.
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def delete_user(userid: str) -> Response[UsersRead]:
        """
        Deletes an existing user by ID.

        Args:
            userid (str): The ID of the user to be deleted.

        Returns:
            Response[UsersRead]: A response object containing information about the deleted user.
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def update_user(userid: str, user: UsersWrite) -> Response[UsersRead]:
        """
        Updates an existing user's information by ID.

        Args:
            userid (str): The ID of the user to be updated.
            user (UsersWrite): The updated data for the user.

        Returns:
            Response[UsersRead]: A response object containing the updated user's information.
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_user_by_id(userid: str) -> Response[UsersRead]:
        """
        Retrieves a user's information by ID.

        Args:
            userid (str): The ID of the user to be retrieved.

        Returns:
            Response[UsersRead]: A response object containing the user's information.
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_all_user() -> Response[UsersRead]:
        """
        Retrieves information of all users.

        Returns:
            Response[UsersRead]: A response object containing a list of all users.
        """
        raise NotImplementedError()