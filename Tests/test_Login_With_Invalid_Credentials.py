from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Page_Objects.Landing_Page import *
from Page_Objects.Time_Tracker_Page import *
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class Test_Login_With_Invalid_Credentials():
    @pytest.fixture(autouse=True)

    def classSetup(self):
        print("title is"+self.driver.title)

    def test_Login_With_Invalid_Credentials(self):
        # Invalid Login Credentials
        username = "invalidusername@invalidusername.com"
        password = "invalidpassword"

        # Creating object of Landing_Page and calling methods inside it by passing Webdriver object.
        Landing_Page_Object = Landing_Page()
        Landing_Page_Object.Login(self.driver, username, password)

        # Creating object of Time_Tracker_Page and calling methods inside it by passing the Webdriver object
        Time_Tracker_Page_Object = Time_Tracker_Page()
        Time_Tracker_Page_Object.Check_If_Login_Succeeded_Or_Failed(self.driver)










