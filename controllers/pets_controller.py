from http import HTTPStatus

import requests

from data_objects.post_pet_request import Pet
from urls.urls import PET_URL, PET_ID_URL


class PetsController:
    @staticmethod
    def create_pet(payload):
        pet = requests.post(PET_URL, json=payload)
        assert pet.status_code == HTTPStatus.OK, \
            f"Pet creation failed. Status code = {pet.status_code}. Msg = {pet.json()}"
        return Pet(**pet.json())

    @staticmethod
    def get_pet_by_id(pet_id):
        pet = requests.get(PET_ID_URL.format(pet_id))
        assert pet.status_code == HTTPStatus.OK, \
            f"Pet retrieval failed. Status code = {pet.status_code}. Msg = {pet.json()}"
        return Pet(**pet.json())

    @staticmethod
    def update_pet(payload):
        pet = requests.put(PET_URL, json=payload)
        assert pet.status_code == HTTPStatus.OK, \
            f"Pet update failed. Status code = {pet.status_code}. Msg = {pet.json()}"
        return Pet(**pet.json())

    @staticmethod
    def delete_pet(pet_id):
        pet = requests.delete(PET_ID_URL.format(pet_id))
        assert pet.status_code == HTTPStatus.OK, \
            f"Pet delete failed. Status code = {pet.status_code}. Msg = {pet.json()}"
