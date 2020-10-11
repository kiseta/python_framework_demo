__author__ = 'tk'

from model.group import Group


def test_modify_first_group_name(app):
    app.group.check_group_present("testname","testheader", "testfooter")
    app.group.modify_first_group(Group(name="Modified Group Name"))


def test_modify_first_group_header(app):
    app.group.check_group_present("testname","testheader", "testfooter")
    app.group.modify_first_group(Group(header="Modified Header"))
