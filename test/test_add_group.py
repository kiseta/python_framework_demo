# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_add_group(app):
    old_groups = app.group.get_group_list()
    print("Original Groups Count: " + str(len(old_groups)))
    s = str(random.randint(111, 999))
    app.group.create(Group(name="grname" + s, header="grheader" + s, footer="grfooter" + s))
    new_groups = app.group.get_group_list()
    print("New Groups Count: " + str(len(new_groups)))
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    print("Original Groups Count: " + str(len(old_groups)))
    app.group.create(Group(name="", header="" , footer=""))
    new_groups = app.group.get_group_list()
    print("New Groups Count: " + str(len(new_groups)))
    assert len(old_groups) + 1 == len(new_groups)
