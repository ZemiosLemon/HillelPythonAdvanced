from faker import Faker


def random_list():
    fake = Faker('ru_RU')

    list_students = [fake.name() for _ in range(10)]
    return list_students
