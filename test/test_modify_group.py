__author__ = 'tk'

from model.group import Group


def test_modify_first_group_name(app):
    app.group.check_group_present("Original Group Name ","Original Header", "Original Footer")

    old_groups = app.group.get_group_list()
    print("Original Groups Count: " + str(len(old_groups)))

    app.group.modify_first_group(Group(name="Modified Group Name"))

    new_groups = app.group.get_group_list()
    print("New Groups Count: " + str(len(new_groups)))
    assert len(old_groups)  == len(new_groups)


def test_modify_first_group_header(app):
    app.group.check_group_present("Original Group Name ","Original Header", "Original Footer")

    old_groups = app.group.get_group_list()
    print("Original Groups Count: " + str(len(old_groups)))

    app.group.modify_first_group(Group(header="Modified Header"))

    new_groups = app.group.get_group_list()
    print("New Groups Count: " + str(len(new_groups)))
    assert len(old_groups)  == len(new_groups)
