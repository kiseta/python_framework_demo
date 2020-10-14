__author__ = 'tk'

from model.group import Group
from random import randrange


def test_modify_first_group_name(app):
    app.group.check_group_present()

    old_groups = app.group.get_group_list()
    print("Original Groups Count: " + str(len(old_groups)))
    index = randrange(len(old_groups))
    group = Group(name="Modified Group Name")
    app.group.modify_group_by_index(index, group)
    group.id = old_groups[index].id
    new_groups = app.group.get_group_list()
    print("New Groups Count: " + str(len(new_groups)))
    assert len(old_groups)  == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_first_group_header(app):
#     app.group.check_group_present("Original Group Name ","Original Header", "Original Footer")
#
#     old_groups = app.group.get_group_list()
#     print("Original Groups Count: " + str(len(old_groups)))
#
#     app.group.modify_first_group(Group(header="Modified Header"))
#
#     new_groups = app.group.get_group_list()
#     print("New Groups Count: " + str(len(new_groups)))
#     assert len(old_groups)  == len(new_groups)
