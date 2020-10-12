__author__ = 'tk'


def test_delete_first_group(app):
    app.group.check_group_present("Test Name","Test Header", "Test Footer")

    old_groups = app.group.get_group_list()
    print("Original Groups Count: " + str(len(old_groups)))

    app.group.delete_first_group()

    new_groups = app.group.get_group_list()
    print("New Groups Count: " + str(len(new_groups)))
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

