# -*- coding: utf-8 -*-
__author__ = 'tk'

from model.contact import Contact
import pytest
from data.add_contact import fakedata


@pytest.mark.parametrize("contact", fakedata, ids=[repr(x) for x in fakedata])
def test_add_new_contact(app, contact):
    app.contact.create(contact)
