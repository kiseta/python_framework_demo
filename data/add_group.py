__author__ = 'tk'

import random
import string
from model.group import Group
from faker import Faker

fake = Faker('en_US')

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header3", footer="footer4")
]

fakedata = [
    Group(name=fake.pystr_format(), header=fake.pystr(), footer=fake.pystr_format()),
    Group(name=fake.pystr(), header=fake.pystr_format(), footer=fake.pystr())
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]
