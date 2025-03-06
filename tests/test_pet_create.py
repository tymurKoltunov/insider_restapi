import pytest

from controllers.pets_controller import PetsController
from payloads.pet_payload import get_pet_payload, get_pet_invalid_name_payload


class TestPetCreation:
    def test_pet_creation_positive(self):
        payload = get_pet_payload()
        pet = PetsController.create_pet(payload)
        assert payload["name"] == pet.name

    def test_pet_creation_negative(self):
        payload = get_pet_invalid_name_payload()
        with pytest.raises(AssertionError) as err:
            PetsController.create_pet(payload)
        assert "something bad happened" in str(err.value)
        assert "500" in str(err.value)
