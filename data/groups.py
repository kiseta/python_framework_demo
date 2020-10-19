__author__ = 'tk'

from model.group import Group
from faker import Faker

fake = Faker('en_US')

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

fakedata = [
    Group(name=fake.pystr_format(), header=fake.pystr(), footer=fake.pystr_format()),
    Group(name=fake.pystr(), header=fake.pystr_format(), footer=fake.pystr())
]

