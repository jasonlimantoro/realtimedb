from django_seed import Seed
from realtimedb.temperature.models import Temperature
from random import uniform


def executor(number):
    seeder = Seed.seeder()

    seeder.add_entity(Temperature, number, {
        'value': lambda x: round(uniform(10, 30), 2),
        'location': lambda x: seeder.faker.city()
    })
    seeder.execute()
