

class Landing_Page():

    def Login(self, driver, username, password):
        print("inside login function")
        driver.implicitly_wait(5)
        Email_Text_Field = driver.find_element_by_id("email")
        Email_Text_Field.send_keys(username)
        Password_Text_Field = driver.find_element_by_id("password")
        Password_Text_Field.send_keys(password)
        Login_Button = driver.find_element_by_class_name("access__panel__content__buttons--login")
        Login_Button.click()
