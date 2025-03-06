import pytest

from controllers.pets_controller import PetsController
from payloads.pet_payload import get_pet_payload


class TestPetDelete:
    def test_pet_delete_positive(self):
        payload = get_pet_payload()
        created_pet = PetsController.create_pet(payload)
        PetsController.delete_pet(created_pet.id)
        with pytest.raises(AssertionError) as err:
            PetsController.get_pet_by_id(created_pet.id)
        assert "Pet not found" in str(err)

    def test_pet_delete_negative(self):
        invalid_id = "qweryy"
        with pytest.raises(AssertionError) as err:
            PetsController.delete_pet(invalid_id)
        assert "NumberFormatException" in str(err)