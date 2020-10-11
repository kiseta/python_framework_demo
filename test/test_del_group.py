__author__ = 'tk'


def test_delete_first_group(app):
    app.group.check_group_present("testname","testheader", "testfooter")
    app.group.delete_first_group()

