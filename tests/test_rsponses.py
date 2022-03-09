class TestCreateUser:
    def test_new_user(self, new_user):
        """Test of user creation"""
        response = new_user
        assert response.status_code == 200


class TestLoginUser:
    def test_login(self, login_user):
        """Test of user creation"""
        response = login_user
        assert response.status_code == 200


class TestFindUser:
    def test_find_user(self, find_user):
        """User search test"""
        response = find_user
        assert response.status_code == 200


class TestLogoutUser:
    def test_logout_user(self, logout_user):
        """Test logout"""
        response = logout_user
        assert response.status_code == 200


class TestDeleteUser:
    def test_delete_user(self, delete_user):
        """Test delete user"""
        response = delete_user
        assert response.status_code == 200


class TestAddPet:
    def test_add(self, add_pet):
        """Test of user creation"""
        response = add_pet
        assert response.status_code == 200


class TestFindPet:
    def test_find_pet(self, find_pet):
        """Pet search test"""
        response = find_pet
        assert response.status_code == 200


class TestuUpdatePet:
    def test_update_pet(self, update_pet):
        """Update pet test"""
        response = update_pet
        assert response.status_code == 200


class TestFindUpdatePet:
    def test_find_pet(self, find_update_pet):
        """Pet search test"""
        response = find_update_pet
        assert response.status_code == 200
