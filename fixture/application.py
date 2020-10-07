__author__ = "tk"

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def delete_group(self):
        wd = self.wd
        # delete new group
        # wd.find_element_by_xpath("//input[@title='Select (" + groupName + ")'").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()


    def destroy(self):
        self.wd.quit()
