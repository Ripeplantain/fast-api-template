from fastapi import APIRouter
from src.dtos.response import Response
from src.dtos.read.users import UsersRead
from src.dtos.write.users import UsersWrite
from src.services.users_sv import UsersService

router = APIRouter(tags=["user"])

@router.post("/user")
async def create_user(user: UsersWrite) -> Response[UsersRead]:
    """
    Creates a new user.

    Args:
        user (UsersWrite): An object containing the information of the user to be created.

    Returns:
        Response[UsersRead]: A response containing the created user's information.
    """
    return UsersService.add_user(user=user)

@router.delete("/user")
async def delete_user(userid: str) -> Response[UsersRead]:
    """
    Deletes an existing user by ID.

    Args:
        userid (str): The ID of the user to be deleted.

    Returns:
        Response[UsersRead]: A response indicating the status of the deletion operation.
    """
    return UsersService.delete_user(userid=userid)

@router.put("/user")
async def update_user(userid: str, user: UsersWrite) -> Response[UsersRead]:
    """
    Updates the information of an existing user by ID.

    Args:
        userid (str): The ID of the user to be updated.
        user (UsersWrite): An object containing the updated information of the user.

    Returns:
        Response[UsersRead]: A response containing the updated user's information.
    """
    return UsersService.update_user(userid=userid, user=user)

@router.get("/user/{userid}")
async def get_user_by_id(userid: str) -> Response[UsersRead]:
    """
    Retrieves user information by ID.

    Args:
        userid (str): The ID of the user to be retrieved.

    Returns:
        Response[UsersRead]: A response containing the retrieved user's information.
    """
    return UsersService.get_user_by_id(userid=userid)

@router.get("/user")
async def get_all_user() -> Response[UsersRead]:
    """
    Retrieves information of all users.

    Returns:
        Response[UsersRead]: A response containing information for all users.
    """
    return UsersService.get_all_user()