from selenium import webdriver

class Login():
    def Login(self):
        URL = "https://clockify.me/login"
        driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe")
        driver.get(URL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        Email_Text_Field = driver.find_element_by_id("email")
        Email_Text_Field.send_keys("pruthvi2k1@yahoo.com")
        Password_Text_Field = driver.find_element_by_id("password")
        Password_Text_Field.send_keys("pruthviraj")
        Login_Button = driver.find_element_by_class_name("access__panel__content__buttons--login")
        Login_Button.click()
        #checking if manual mode button exists after login. It will exist if login succeeds
        Manual_Mode_Button = driver.find_element_by_xpath("//button[@title='Manual Mode']")


Login=Login()
Login.Login()