from selenium.webdriver.common.action_chains import ActionChains

class Time_Tracker_Page():

    def Check_If_Login_Succeeded_Or_Failed(self, driver):
        try:
            driver.implicitly_wait(5)
            Manual_Mode_Button = driver.find_element_by_xpath("//button[@title='Manual Mode']")
            print("Login Succeeded")
        except:
            driver.find_element_by_xpath("/html/body/app-root/login/login-clockify/div/div[1]/div/div[2]/form/div[2]/div[2]/span")
            print("Login Failed and test case passed")


    def Logout(self, driver):
        element_to_hover_over = driver.find_element_by_link_text('Pruthvi2k1')
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.find_element_by_link_text('Log out').click()
        # checking if Login button exists after logout. It will exist if logout succeeds
        driver.find_element_by_class_name("access__panel__content__buttons--login")
