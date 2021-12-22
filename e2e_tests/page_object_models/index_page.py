from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class IndexPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "inputUserName")
        return element

    def select_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "inputPassword")
        return element

    def select_sign_in_button(self):
        element: WebElement = self.driver.find_element(By.ID, "signInButton")
        return element
