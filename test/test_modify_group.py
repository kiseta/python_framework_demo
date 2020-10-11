__author__ = 'tk'

from model.group import Group


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="New Group"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="New Header"))
