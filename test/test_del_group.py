__author__ = 'tk'
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Del Group"))
    app.group.delete_first_group()
