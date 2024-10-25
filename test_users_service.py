import unittest
from unittest.mock import patch
from src.dtos.write.users import UsersWrite
from src.services.users_sv import UsersService

class TestUsersService(unittest.TestCase):
    """
    Test suite for the UsersService class, covering various scenarios for user operations.
    """

    @patch('src.repositories.users_rp.UsersRepository.add_user')
    def test_add_user_success(self, mock_add_user):
        """
        Test the successful addition of a user.

        Mocks the add_user method to simulate a successful user addition 
        and asserts the correct response message and data.
        """
        # Arrange
        user_data = UsersWrite(fullname="John Doe", email="john@example.com", location="USA", age=30)
        mock_add_user.return_value = None

        # Act
        response = UsersService.add_user(user_data)

        # Assert
        self.assertEqual(response.message, "user created")
        self.assertIsNotNone(response.data)
        self.assertEqual(response.data[0].fullname, "John Doe")

    @patch('src.repositories.users_rp.UsersRepository.add_user')
    def test_add_user_data_error(self, mock_add_user):
        """
        Test the addition of a user with invalid data.

        Mocks the add_user method to simulate a ValueError and asserts 
        that the response indicates a data processing error.
        """
        # Arrange
        user_data = UsersWrite(fullname=None, email="john@example.com", location="USA", age=30)
        mock_add_user.side_effect = ValueError("Invalid data")

        # Act
        response = UsersService.add_user(user_data)

        # Assert
        self.assertEqual(response.message, "an error occurred while processing user data")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.add_user')
    def test_add_user_connection_error(self, mock_add_user):
        """
        Test the addition of a user when there is a database connection error.

        Mocks the add_user method to simulate a ConnectionError and asserts 
        that the response indicates a database connection failure.
        """
        # Arrange
        user_data = UsersWrite(fullname="John Doe", email="john@example.com", location="USA", age=30)
        mock_add_user.side_effect = ConnectionError("Connection error")

        # Act
        response = UsersService.add_user(user_data)

        # Assert
        self.assertEqual(response.message, "failed to connect to the database")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    @patch('src.repositories.users_rp.UsersRepository.delete_user')
    def test_delete_user_success(self, mock_delete_user, mock_get_user_by_id):
        """
        Test the successful deletion of a user.

        Mocks the get_user_by_id and delete_user methods to simulate 
        a successful user deletion and asserts the correct response message and data.
        """
        # Arrange
        userid = "test-user-id"
        user_data = ("test-user-id", "John Doe", 30, "john@example.com", "USA")
        mock_get_user_by_id.return_value = user_data

        # Act
        response = UsersService.delete_user(userid)

        # Assert
        self.assertEqual(response.message, "user deleted")
        self.assertIsNotNone(response.data)
        self.assertEqual(response.data[0].id, "test-user-id")
        self.assertEqual(response.data[0].fullname, "John Doe")

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_delete_user_not_found(self, mock_get_user_by_id):
        """
        Test the deletion of a user that does not exist.

        Mocks the get_user_by_id method to simulate a scenario where 
        the user is not found and asserts that the correct response is returned.
        """
        # Arrange
        userid = "non-existent-user-id"
        mock_get_user_by_id.return_value = None

        # Act
        response = UsersService.delete_user(userid)

        # Assert
        self.assertEqual(response.message, "user not found")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_delete_user_data_error(self, mock_get_user_by_id):
        """
        Test the deletion of a user with an invalid ID.

        Mocks the get_user_by_id method to simulate a ValueError and asserts 
        that the response indicates a data processing error.
        """
        # Arrange
        userid = "test-user-id"
        mock_get_user_by_id.side_effect = ValueError("Invalid user ID")

        # Act
        response = UsersService.delete_user(userid)

        # Assert
        self.assertEqual(response.message, "an error occurred while processing user data")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_delete_user_connection_error(self, mock_get_user_by_id):
        """
        Test the deletion of a user when there is a database connection error.

        Mocks the get_user_by_id method to simulate a ConnectionError and asserts 
        that the response indicates a database connection failure.
        """
        # Arrange
        userid = "test-user-id"
        mock_get_user_by_id.side_effect = ConnectionError("Connection error")

        # Act
        response = UsersService.delete_user(userid)

        # Assert
        self.assertEqual(response.message, "failed to connect to the database")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    @patch('src.repositories.users_rp.UsersRepository.update_user')
    def test_update_user_success(self, mock_update_user, mock_get_user_by_id):
        """
        Test the successful update of a user.

        Mocks the get_user_by_id and update_user methods to simulate 
        a successful user update and asserts the correct response message and data.
        """
        # Arrange
        userid = "test-user-id"
        user_data = UsersWrite(fullname="Jane Doe", email="jane@example.com", location="Canada", age=28)
        mock_get_user_by_id.return_value = ("test-user-id", "John Doe", 30, "john@example.com", "USA")

        # Act
        response = UsersService.update_user(userid, user_data)

        # Assert
        self.assertEqual(response.message, "user updated")
        self.assertEqual(response.data[0].fullname, "Jane Doe")

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_update_user_not_found(self, mock_get_user_by_id):
        """
        Test the update of a user that does not exist.

        Mocks the get_user_by_id method to simulate a scenario where 
        the user is not found and asserts that the correct response is returned.
        """
        # Arrange
        userid = "non-existent-user-id"
        user_data = UsersWrite(fullname="Jane Doe", email="jane@example.com", location="Canada", age=28)
        mock_get_user_by_id.return_value = None

        # Act
        response = UsersService.update_user(userid, user_data)

        # Assert
        self.assertEqual(response.message, "user does not exist")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_update_user_data_error(self, mock_get_user_by_id):
        """
        Test the update of a user with an invalid ID.

        Mocks the get_user_by_id method to simulate a ValueError and asserts 
        that the response indicates a data processing error.
        """
        # Arrange
        userid = "test-user-id"
        user_data = UsersWrite(fullname="Jane Doe", email="jane@example.com", location="Canada", age=28)
        mock_get_user_by_id.side_effect = ValueError("Invalid user ID")

        # Act
        response = UsersService.update_user(userid, user_data)

        # Assert
        self.assertEqual(response.message, "an error occurred while processing user data")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_update_user_connection_error(self, mock_get_user_by_id):
        """
        Test the update of a user when there is a database connection error.

        Mocks the get_user_by_id method to simulate a ConnectionError and asserts 
        that the response indicates a database connection failure.
        """
        # Arrange
        userid = "test-user-id"
        user_data = UsersWrite(fullname="Jane Doe", email="jane@example.com", location="Canada", age=28)
        mock_get_user_by_id.side_effect = ConnectionError("Connection error")

        # Act
        response = UsersService.update_user(userid, user_data)

        # Assert
        self.assertEqual(response.message, "failed to connect to the database")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_get_user_by_id_success(self, mock_get_user_by_id):
        """
        Test the retrieval of a user by ID.

        Mocks the get_user_by_id method to simulate a successful retrieval 
        and asserts the correct response message and data.
        """
        # Arrange
        userid = "test-user-id"
        mock_get_user_by_id.return_value = ("test-user-id", "John Doe", 30, "john@example.com", "USA")

        # Act
        response = UsersService.get_user_by_id(userid)

        # Assert
        self.assertEqual(response.message, "user found")
        self.assertEqual(response.data[0].id, "test-user-id")

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_get_user_by_id_not_found(self, mock_get_user_by_id):
        """
        Test the retrieval of a user by ID that does not exist.

        Mocks the get_user_by_id method to simulate a scenario where 
        the user is not found and asserts that the correct response is returned.
        """
        # Arrange
        userid = "non-existent-user-id"
        mock_get_user_by_id.return_value = None

        # Act
        response = UsersService.get_user_by_id(userid)

        # Assert
        self.assertEqual(response.message, "user does not exist")
        self.assertEqual(response.data, [])

    @patch('src.repositories.users_rp.UsersRepository.get_user_by_id')
    def test_get_user_by_id_connection_error(self, mock_get_user_by_id):
        """
        Test the retrieval of a user by ID when there is a database connection error.

        Mocks the get_user_by_id method to simulate a ConnectionError and asserts 
        that the response indicates a database connection failure.
        """
        # Arrange
        userid = "test-user-id"
        mock_get_user_by_id.side_effect = ConnectionError("Connection error")

        # Act
        response = UsersService.get_user_by_id(userid)

        # Assert
        self.assertEqual(response.message, "failed to connect to the database")
        self.assertEqual(response.data, [])