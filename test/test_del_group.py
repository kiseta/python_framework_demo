__author__ = 'tk'
from model.group import Group
from random import randrange


def test_delete_random_group(app):
    app.group.check_group_present("Test Name","Test Header", "Test Footer")

    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))
    print("Original Groups Count: " + str(len(old_groups)))
    print("Random Index: " + str(index))
    app.group.delete_group_by_index(index)

    new_groups = app.group.get_group_list()
    print("New Groups Count: " + str(len(new_groups)))
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups

