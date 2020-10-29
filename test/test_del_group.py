__author__ = 'tk'
from model.group import Group
from random import randrange
import random

# validation viA UI
# def test_delete_random_group(app):
#     app.group.check_group_present()
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     print("Original Groups Count: " + str(len(old_groups)))
#     print("Random Index: " + str(index))
#     app.group.delete_group_by_index(index)
#     new_groups = app.group.get_group_list()
#     print("New Groups Count: " + str(len(new_groups)))
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[index:index+1] = []
#     assert old_groups == new_groups

#validation via DB
#choose element by id
def test_delete_group(app, db, check_ui=True):
    app.group.check_group_present()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)