# -*- coding: utf-8 -*-
from fixture.group import GROUP
from fixture.group import GROUP_BLANK
from model.group import Group
import pytest
from data.add_group import fakedata as testdata

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     print("Original Groups Count: " + str(len(old_groups)))
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     print("New Groups Count: " + str(len(new_groups)))
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)