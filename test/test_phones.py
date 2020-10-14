import re

def test_phones_on_home_page(app):
        contact_from_home_page = app.contact.get_contact_list()[0]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
        assert clear(contact_from_home_page.homephone) == clear(contact_from_edit_page.homephone)
        assert clear(contact_from_home_page.workphone) == clear(contact_from_edit_page.workphone)
        assert clear(contact_from_home_page.mobilephone) == clear(contact_from_edit_page.mobilephone)
        assert clear(contact_from_home_page.secondaryphone) == clear(contact_from_edit_page.secondaryphone)

def clear(s):
    return re.sub("[() -.+]", "", s)