__author__ = "tk"


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        # init group create
        wd.find_element_by_name("new").click()
        # fill out new group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # group create submit
        wd.find_element_by_name("submit").click()
        # return to group page
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        # navigate to group page
        wd.find_element_by_link_text("group page").click()
