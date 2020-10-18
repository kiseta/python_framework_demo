from model.contact import Contact
from faker import Faker
fake = Faker('en_US')


def generate_contact_data():
    global CONTACT
    CONTACT = Contact(firstname=fake.first_name(), lastname=fake.last_name(),
                      address=fake.address(), homephone=fake.phone_number(),
                      mobilephone=fake.phone_number(), workphone=fake.phone_number(),
                      email=fake.email(), secondaryphone=fake.phone_number())


def test_add_new_contact(app):
    for i in range(3):
        generate_contact_data()
        app.contact.create(CONTACT)
