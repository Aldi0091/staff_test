from django_seed import Seed
from faker import Faker
import random

from main.models import Staff


def first_rec():
    e = Staff(
        name='Смирнов Андрей Иванович',
        position='Генеральный директор',
        emp_date='2016-06-11',
        salary='500000'
    )
    e.save()


def fill_emp(count, pos, year, salary, parent_min, parent_max):
    seeder = Seed.seeder()
    fake = Faker('ru_RU')
    with Staff.objects.disable_mptt_updates():
        seeder.add_entity(Staff, count, {
            'name': lambda x: fake.name(),
            'position': pos,
            'emp_date': '{}-{}-{}'.format(year, random.randint(1, 12), random.randint(1, 28)),
            'salary': lambda x: random.randint(salary-25000, salary+25000),
            'parent': lambda x: Staff.objects.get(id=random.randint(parent_min, parent_max)),
        })
        seeder.execute()


def del_obj():
    with Staff.objects.disable_mptt_updates():
        objs = Staff.objects.all()
        objs.delete()
    Staff.objects.rebuild()


def run():
    first_rec()
    fill_emp(10, 'Региональный директор', 2017, 340000, 1, 1)
    fill_emp(100, 'Топ менеджер', 2018, 240000, 2, 11)
    fill_emp(1000, 'Менеджер', 2019, 160000, 12, 111)
    fill_emp(40000, 'Младший менеджер', 2020, 120000, 112, 1111)
    fill_emp(10000, 'Стажер', 2021, 100000, 1112, 41111)
    Staff.objects.rebuild()
    pass