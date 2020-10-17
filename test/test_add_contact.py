from model.contact import Contact
from faker import Faker
faker = Faker('en_US')


def generate_contact_data():
    global CONTACT
    CONTACT = Contact(firstname=faker.first_name(), lastname=faker.last_name(),
                      address=faker.address(), homephone=faker.phone_number(),
                      mobilephone=faker.phone_number(), workphone=faker.phone_number(),
                      email=faker.email(), secondaryphone=faker.phone_number())


def test_add_new_contact(app):
    for i in range(3):
        generate_contact_data()
        app.contact.create(CONTACT)
