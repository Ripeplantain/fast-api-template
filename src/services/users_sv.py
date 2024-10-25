import uuid
import logging
from src.dtos.response import Response
from src.dtos.read.users import UsersRead
from src.dtos.write.users import UsersWrite
from src.repositories.users_rp import UsersRepository
from src.services.users_ab import UsersAbstractService

# Configuring the logging settings
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class UsersService(UsersAbstractService):
    """
    A service class for managing user-related operations.

    This class implements the abstract service methods for handling users, including
    adding, deleting, updating, and fetching users by interacting with the repository.
    """

    @staticmethod
    def add_user(user: UsersWrite) -> Response[UsersRead]:
        """
        Adds a new user to the database.

        Args:
            user (UsersWrite): The data of the user to be added.

        Returns:
            Response[UsersRead]: A response object containing the created user's information.
        """
        try:
            _id = str(uuid.uuid4())
            UsersRepository.add_user(user, _id)

            return Response[UsersRead](
                message="user created", 
                data=[UsersRead(
                    id=_id,
                    **user.model_dump()
                )]
            )
        except (ValueError, TypeError) as e:
            logging.error("Data error occurred: %s",e)
            return Response[UsersRead](
                message="an error occurred while processing user data", 
                data=[]
            )
        except ConnectionError as e:
            logging.error("Database connection error: %s",e)
            return Response[UsersRead](
                message="failed to connect to the database", 
                data=[]
            )

    @staticmethod
    def delete_user(userid: str) -> Response[UsersRead]:
        """
        Deletes an existing user by ID.

        Args:
            userid (str): The ID of the user to be deleted.

        Returns:
            Response[UsersRead]: A response indicating the deletion status and user information.
        """
        try:
            does_user_exists = UsersRepository.get_user_by_id(userid=userid)

            if does_user_exists:
                UsersRepository.delete_user(userid)
                return Response[UsersRead](
                    message="user deleted", 
                    data=[UsersRead(
                        id=does_user_exists[0],
                        fullname=does_user_exists[1],
                        email=does_user_exists[3],
                        location=does_user_exists[4],
                        age=does_user_exists[2]
                    )]
                )

            return Response[UsersRead](
                message="user not found", 
                data=[]
            )
        except (ValueError, TypeError) as e:
            logging.error("Data error occurred: %s",e)
            return Response[UsersRead](
                message="an error occurred while processing user data", 
                data=[]
            )
        except ConnectionError as e:
            logging.error("Database connection error: %s",e)
            return Response[UsersRead](
                message="failed to connect to the database", 
                data=[]
            )

    @staticmethod
    def update_user(userid: str, user: UsersWrite) -> Response[UsersRead]:
        """
        Updates an existing user's information by ID.

        Args:
            userid (str): The ID of the user to be updated.
            user (UsersWrite): The updated user data.

        Returns:
            Response[UsersRead]: A response object containing the updated user's information.
        """
        try:
            does_user_exists = UsersRepository.get_user_by_id(userid=userid)
            if does_user_exists:
                UsersRepository.update_user(userid=userid, user=user)
                return Response[UsersRead](
                    message="user updated", 
                    data=[UsersRead(
                        id=userid,
                        **user.model_dump()
                    )]
                )
            
            return Response[UsersRead](
                message="user does not exist", 
                data=[]
            )
        except (ValueError, TypeError) as e:
            logging.error("Data error occurred: %s",e)
            return Response[UsersRead](
                message="an error occurred while processing user data", 
                data=[]
            )
        except ConnectionError as e:
            logging.error("Database connection error: %s",e)
            return Response[UsersRead](
                message="failed to connect to the database", 
                data=[]
            )

    @staticmethod
    def get_user_by_id(userid: str) -> Response[UsersRead]:
        """
        Retrieves a user's information by ID.

        Args:
            userid (str): The ID of the user to be retrieved.

        Returns:
            Response[UsersRead]: A response object containing the user's information.
        """
        try:
            response = UsersRepository.get_user_by_id(userid=userid)
            if response:
                return Response[UsersRead](
                    message="user found", 
                    data=[UsersRead(
                        id=response[0],
                        fullname=response[1],
                        email=response[3],
                        location=response[4],
                        age=response[2]
                    )]
                )
            
            return Response[UsersRead](
                message="user does not exist", 
                data=[]
            )
        except (ValueError, TypeError) as e:
            logging.error("Data error occurred: %s",e)
            return Response[UsersRead](
                message="an error occurred while processing user data", 
                data=[]
            )
        except ConnectionError as e:
            logging.error("Database connection error: %s",e)
            return Response[UsersRead](
                message="failed to connect to the database", 
                data=[]
            )

    @staticmethod
    def get_all_user() -> Response[UsersRead]:
        """
        Retrieves information of all users in the database.

        Returns:
            Response[UsersRead]: A response object containing a list of all users.
        """
        try:
            response = UsersRepository.get_all_user()
            if response:
                users_list = [
                    UsersRead(
                        id=user[0],
                        fullname=user[1],
                        email=user[3],
                        location=user[4],
                        age=user[2]
                    ) for user in response
                ]
                return Response[UsersRead](
                    message="users found",
                    data=users_list
                )
            return Response[UsersRead](
                message="no users found", 
                data=[]
            )
        except (ValueError, TypeError) as e:
            logging.error("Data error occurred: %s",e)
            return Response[UsersRead](
                message="an error occurred while processing user data", 
                data=[]
            )
        except ConnectionError as e:
            logging.error("Database connection error: %s",e)
            return Response[UsersRead](
                message="failed to connect to the database", 
                data=[]
            )