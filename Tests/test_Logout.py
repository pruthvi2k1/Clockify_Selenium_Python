from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Page_Objects.Landing_Page import *
from Page_Objects.Time_Tracker_Page import *
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class Test_Logout():
    @pytest.fixture(autouse=True)

    def classSetup(self):
        print("title is"+self.driver.title)

    def test_Logout(self):
        # Valid Login Credentials
        username = "pruthvi2k1@yahoo.com"
        password = "pruthviraj"

        # Creating object of Landing_Page and calling methods inside it by passing Webdriver object.
        Landing_Page_Object = Landing_Page()
        Landing_Page_Object.Login(self.driver, username, password)

        # Creating object of Time_Tracker_Page and calling methods inside it by passing the Webdriver object
        Time_Tracker_Page_Object = Time_Tracker_Page()
        Time_Tracker_Page_Object.Logout(self.driver)







