from random import randint

from faker import Faker


def create_no():
    return randint(1, 99)


def create_name():
    return Faker().name()
