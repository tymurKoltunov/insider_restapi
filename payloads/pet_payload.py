from faker import Faker

fake = Faker()


def get_pet_payload():
    return {
        "name": fake.first_name(),
        "status": fake.random_element(["available", "pending", "sold"]),
        "photoUrls": [fake.image_url()],
        "category": {"name": fake.word()},
        "tags": [{"name": fake.word()}]
    }


def get_pet_invalid_name_payload():
    return {
        "photoUrls": 123
    }
