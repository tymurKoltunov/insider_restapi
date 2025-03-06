import pytest

from controllers.pets_controller import PetsController
from payloads.pet_payload import get_pet_payload


class TestPetRead:
    def test_get_pet_positive(self):
        payload = get_pet_payload()
        created_pet = PetsController.create_pet(payload)
        retr_pet = PetsController.get_pet_by_id(created_pet.id)
        assert created_pet.name == retr_pet.name

    def test_get_pet_negative(self):
        invalid_id = "sfsfsfsdf"
        with pytest.raises(AssertionError) as err:
            PetsController.get_pet_by_id(invalid_id)
        assert "NumberFormatException" in str(err.value)

