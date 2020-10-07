__author__ = 'tk'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # init group create
        wd.find_element_by_name("new").click()
        # fill out new group form
        self.enter_name(group, wd)
        self.enter_header(group, wd)
        self.enter_footer(group, wd)
        # group create submit
        wd.find_element_by_name("submit").click()
        # return to group page
        self.return_to_groups_page()

    def enter_footer(self, group, wd):
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def enter_header(self, group, wd):
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)

    def enter_name(self, group, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        # navigate to group page
        wd.find_element_by_link_text("group page").click()
