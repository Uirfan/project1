from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class EmployeePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_create_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementModal")
        return element

    def select_expense_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "expenseName")
        return element

    def select_expense_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "expenseAmount")
        return element

    def select_expense_reason_input(self):
        element: WebElement = self.driver.find_element(By.ID, "expenseReason")
        return element

    def select_save_button(self):
        element: WebElement = self.driver.find_element(By.ID, "saveChangesButton")
        return element

    def select_reimbursement_employee(self):
        element: WebElement = self.driver.find_element(By.XPATH, '// *[ @ id = "tableContainerchild"] / tr[2]')
        return element

    def select_sign_out_button(self):
        element: WebElement = self.driver.find_element(By.ID, "signOut")
        return element

    def select_reimbursement_table_employee(self):
        element: WebElement = self.driver.find_element(By.ID, "tableContainerchild")
        return element

    def select_created_reimbursement(self):
        element: WebElement = self.driver.find_element(By.XPATH, '//*[@id="tableContainerchild"]/tr[last()]/td[3]')
        return element
