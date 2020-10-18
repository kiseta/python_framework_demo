__author__ = 'tk'

from model.contact import Contact
from faker import Faker


fake = Faker('en_US')

fakedata = [
    Contact(firstname=fake.first_name(), lastname=fake.last_name(),
            address=fake.address(), homephone=fake.phone_number(),
            mobilephone=fake.phone_number(), workphone=fake.phone_number(),
            email=fake.email(), secondaryphone=fake.phone_number())
    for i in range(5)
]
