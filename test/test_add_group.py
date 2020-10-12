# -*- coding: utf-8 -*-
from model.group import Group
import random
from sys import maxsize


def test_add_group(app):
    old_groups = app.group.get_group_list()
    print("Original Groups Count: " + str(len(old_groups)))
    s = str(random.randint(111, 999))
    group = Group(name="grname" + s, header="grheader" + s, footer="grfooter" + s)
    app.group.create(group)
    new_groups = app.group.get_group_list()
    print("New Groups Count: " + str(len(new_groups)))
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)

    def id_or_max(gr):
        if gr.id:
                return int(gr.id)
        else:
            return maxsize
    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     print("Original Groups Count: " + str(len(old_groups)))
#     app.group.create(Group(name="", header="" , footer=""))
#     new_groups = app.group.get_group_list()
#     print("New Groups Count: " + str(len(new_groups)))
#     assert len(old_groups) + 1 == len(new_groups)
