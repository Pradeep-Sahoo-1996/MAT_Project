from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.__driver = driver
        self.__username = (By.ID, "username")
        self.__password = (By.ID, "password")
        self.__login_button = (By.XPATH, "//button[contains(text(),'Login')]")

    def enter_username(self, username):
        self.__driver.find_element(*self.__username).send_keys(username)

    def enter_password(self, password):
        self.__driver.find_element(*self.__password).send_keys(password)

    def click_login_button(self):
        self.__driver.find_element(*self.__login_button).click()

class TestLogin:
    def setup_method(self):
        self.__driver = webdriver.Chrome()
        self.__driver.get("https://sakshingp.github.io/assignment/login.html")
        self.__driver.maximize_window()

    def test_login(self):
        login_page = LoginPage(self.__driver)
        login_page.enter_username("testuser")
        login_page.enter_password("testpassword")
        login_page.click_login_button()
        WebDriverWait(self.__driver, 10).until(EC.url_to_be("https://sakshingp.github.io/assignment/success.html"))

    def teardown_method(self):
        self.__driver.quit()

if __name__ == "__main__":
    test_login = TestLogin()
    test_login.setup_method()
    test_login.test_login()
    test_login.teardown_method()
# In this program, we create a LoginPage class which has methods for entering the
#  username, password, and clicking the login button. We use encapsulation to make 
# the driver, username, password, and login_button variables private by prefixing
#  them with two underscores. We also create a TestLogin class which uses the 
# LoginPage class to perform the login functionality. We use the webdriver module
#  to open the URL and perform the login actions, and the pytest module to run the tests.

# Note that the private variables in the LoginPage class can only be accessed 
# within the class itself, not outside of it. This helps to prevent accidental 
# changes or misuse of these variables.