import pytest
from selenium import webdriver

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request):
    print("Running one time setUp")
    #if browser == 'firefox':
    # Creating Webdriver Object with needed URL
    URL = "https://clockify.me/login"
    driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe")
    driver.get(URL)
    driver.maximize_window()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

