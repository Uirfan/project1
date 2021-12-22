from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ManagerPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_pending_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "pendingReimbursements")
        return element

    def select_accepted_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "acceptedReimbursements")
        return element

    def select_rejected_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "rejectedReimbursements")
        return element

    def select_a_pending_reimbursement(self):
        element: WebElement = self.driver.find_element(By.XPATH, '// *[ @ id = "tableContainerchild"] / tr[2]')
        return element

    def select_status_dropdown(self):
        element = Select(self.driver.find_element(By.ID, "inputGroupSelect01"))
        return element

    def select_reason_input(self):
        element: WebElement = self.driver.find_element(By.ID, "exampleFormControlTextarea1")
        return element

    def select_save_button(self):
        element: WebElement = self.driver.find_element(By.ID, "saveButton")
        return element

    def select_sign_out_button(self):
        element: WebElement = self.driver.find_element(By.ID, "signOut")
        return element

    def select_stats(self):
        element: WebElement = self.driver.find_element(By.ID, "viewStats")
        return element
    def select_last_reimbursement(self):
        element: WebElement = self.driver.find_element(By.XPATH, '// *[ @ id = "tableContainerchild"] / tr[last()]')
        return element
    def select_last_reimbursement_reason(self):
        element: WebElement = self.driver.find_element(By.XPATH, '//*[@id="checkReimbursements"]/li[2]')
        return element

    def select_last_reimbursement_status(self):
        element: WebElement = self.driver.find_element(By.XPATH, '//*[@id="tableContainerchild"]/tr[last()]/td[6]')
        return element
