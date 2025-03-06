import pytest

from controllers.pets_controller import PetsController
from payloads.pet_payload import get_pet_payload


class TestPetUpdate:
    def test_pet_update_positive(self):
        payload = get_pet_payload()
        updated_name = "updated"
        created_pet = PetsController.create_pet(payload)
        payload["name"] = updated_name
        updated_pet = PetsController.update_pet(payload)
        assert updated_pet.name == updated_name

    def test_pet_update_negative(self):
        payload = get_pet_payload()
        invalid_id = "34fds"
        updated_name = "updated"
        created_pet = PetsController.create_pet(payload)
        payload["name"] = updated_name
        payload["id"] = invalid_id
        with pytest.raises(AssertionError) as err:
            PetsController.update_pet(payload)
        assert "something bad happened" in str(err.value)
        assert "500" in str(err.value)