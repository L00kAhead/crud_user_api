from faker import Faker
import random
from model.models import User, Gender, Role

faker = Faker()
random.seed(101)

def generate_dummy_user():
    first_name = faker.first_name()
    last_name = faker.last_name()
    gender = random.choice(list(Gender))
    roles = [random.choice(list(Role))]
    return User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        roles=roles
    )

dummy_users = [generate_dummy_user() for _ in range(25)]
