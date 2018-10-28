from selenium import webdriver
import re

class Login_Invalid():
    def Login_Invalid(self):
        URL = "https://clockify.me/login"
        driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe")
        driver.get(URL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        Email_Text_Field = driver.find_element_by_id("email")
        Email_Text_Field.send_keys("InvalidEmail@InvalidEmail.com")
        Password_Text_Field = driver.find_element_by_id("password")
        Password_Text_Field.send_keys("InvalidPassword")
        Login_Button = driver.find_element_by_class_name("access__panel__content__buttons--login")
        Login_Button.click()
        driver.find_element_by_xpath("/html/body/app-root/login/login-clockify/div/div[1]/div/div[2]/form/div[2]/div[2]/span")
        




Login_Invalid=Login_Invalid()
Login_Invalid.Login_Invalid()