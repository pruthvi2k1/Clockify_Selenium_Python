from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Page_Objects.Landing_Page import Landing_Page
from Page_Objects.Time_Tracker_Page import *

#Creating Webdriver Object with needed URL

URL = "https://clockify.me/login"
driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe")
driver.get(URL)
driver.maximize_window()

#Valid Login Credentials
username="invalidusername@invalidusername.com"
password="invalidpassword"

# Creating object of Landing_Page and calling methods inside it by passing Webdriver object.
Landing_Page_Object=Landing_Page()
Landing_Page_Object.Login(driver, username, password)

# Creating object of Time_Tracker_Page and calling methods inside it by passing the Webdriver object
Time_Tracker_Page_Object=Time_Tracker_Page()
Time_Tracker_Page_Object.Check_If_Login_Succeeded_Or_Failed(driver)

#Quitting the browser
driver.quit()