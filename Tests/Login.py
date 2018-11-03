from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Login():
    def Login(self):

        driver.implicitly_wait(5)
        Email_Text_Field = driver.find_element_by_id("email")
        Email_Text_Field.send_keys("pruthvi2k1@yahoo.com")
        Password_Text_Field = driver.find_element_by_id("password")
        Password_Text_Field.send_keys("pruthviraj")
        Login_Button = driver.find_element_by_class_name("access__panel__content__buttons--login")
        Login_Button.click()
        #checking if manual mode button exists after login. It will exist if login succeeds
        Manual_Mode_Button = driver.find_element_by_xpath("//button[@title='Manual Mode']")

    def Logout(self):
        try:
            driver.implicitly_wait(5)
            element_to_hover_over = driver.find_element_by_link_text('Pruthvi2k1')
            hover = ActionChains(driver).move_to_element(element_to_hover_over)
            hover.perform()
            driver.find_element_by_link_text('Log out').click()
            # checking if Login button exists after logout. It will exist if logout succeeds
            driver.find_element_by_class_name("access__panel__content__buttons--login")
        except:
            print("Already loged out")

    def Login_Invalid(self):
        driver.implicitly_wait(5)
        Email_Text_Field = driver.find_element_by_id("email")
        Email_Text_Field.send_keys("InvalidEmail@InvalidEmail.com")
        Password_Text_Field = driver.find_element_by_id("password")
        Password_Text_Field.send_keys("InvalidPassword")
        Login_Button = driver.find_element_by_class_name("access__panel__content__buttons--login")
        Login_Button.click()
        driver.find_element_by_xpath("/html/body/app-root/login/login-clockify/div/div[1]/div/div[2]/form/div[2]/div[2]/span")



URL = "https://clockify.me/login"
driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe")
driver.get(URL)
driver.maximize_window()

Login_Object=Login()

Login_Object.Login()
Login_Object.Logout()
Login_Object.Login_Invalid()
driver.quit()