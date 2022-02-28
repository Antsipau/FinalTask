import requests
import pytest


class TestCreateUser:
    """Create user"""
    @pytest.fixture()
    def new_user(self):
        response = requests.post('https://petstore.swagger.io/v2/user', json={"id": 22814228, "username": "ivan_antsipau",
                                                                         "firstName": "ivan", "lastName": "antsipau",
                                                                         "email": "test@test.com", "password": "123",
                                                                         "phone": "+7495000000", "userStatus": 9090})
        return response

    def test_new_user(self, new_user):
        """Test of user creation"""
        response = new_user
        assert response.status_code == 200


class TestLoginUser:
    """login user"""
    @pytest.fixture()
    def login_user(self):
        response = requests.get('https://petstore.swagger.io/v2/user/login?username=ivan_antsipau&password=123',
                                json={"username": "ivan_antsipau", "password": "123"})
        return response

    def test_login(self, login_user):
        """Test of user creation"""
        response = login_user
        assert response.status_code == 200


class TestFindUser:
    """Find user"""
    @pytest.fixture()
    def find_user(self):
        response = requests.get('https://petstore.swagger.io/v2/user/ivan_antsipau')
        return response

    def test_find_user(self, find_user):
        """User search test"""
        response = find_user
        assert response.status_code == 200


class TestLogoutUser:
    """Logout user"""
    @pytest.fixture()
    def logout_user(self):
        response = requests.get('https://petstore.swagger.io/v2/user/logout?username=ivan_antsipau&password=123')
        return response

    def test_logout_user(self, logout_user):
        """Test logout"""
        response = logout_user
        assert response.status_code == 200


class TestDeleteUser:
    """Delete user"""
    @pytest.fixture()
    def delete_user(self):
        response = requests.delete('https://petstore.swagger.io/v2/user/string')
        return response

    def test_delete_user(self, delete_user):
        """Test delete user"""
        response = delete_user
        assert response.status_code == 200


class TestAddPet:
    """Add a pet"""
    @pytest.fixture()
    def add_pet(self):
        response = requests.post('https://petstore.swagger.io/v2/pet',
                                 json={"id": 222222, "category": {"id": 1, "name": "rufus"},
                                       "name": "doggie", "photoUrls": ["some URL"],
                                       "tags": [{"id": 1, "name": "rufus"}],
                                       "status": "available"})
        return response

    def test_add(self, add_pet):
        """Test of user creation"""
        response = add_pet
        assert response.status_code == 200


class TestFindPet:
    """Find a pet"""
    @pytest.fixture()
    def find_pet(self):
        response = requests.get('https://petstore.swagger.io/v2/pet/222222')
        return response

    def test_find_pet(self, find_pet):
        """Pet search test"""
        response = find_pet
        assert response.status_code == 200


class TestuUpdatePet:
    """Update a pet"""
    @pytest.fixture()
    def update_pet(self):
        response = requests.put('https://petstore.swagger.io/v2/pet', json={"id": 222222,
                                                                            "category": {"id": 1, "name": "gizmo"},
                                                                            "name": "doggie", "photoUrls": ["some URL"],
                                                                            "tags": [{"id": 1, "name": "gizmo"}],
                                                                            "status": "available"})
        return response

    def test_update_pet(self, update_pet):
        """Update pet test"""
        response = update_pet
        assert response.status_code == 200


class TestFindUpdatePet:
    """Find updated pet"""
    @pytest.fixture()
    def find_update_pet(self):
        response = requests.get('https://petstore.swagger.io/v2/pet/222222')
        return response

    def test_find_pet(self, find_update_pet):
        """Pet search test"""
        response = find_update_pet
        assert response.status_code == 200








