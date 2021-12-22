from behave.runner import Context
from selenium import webdriver
from page_object_models.index_page import IndexPage
from page_object_models.employee_page import EmployeePage
from page_object_models.manager_page import ManagerPage


def before_all(context: Context):

    context.driver = webdriver.Chrome("chromedriver.exe")
    context.driver.set_window_size(1920, 1080)
    context.index_page = IndexPage(context.driver)
    context.employee_page = EmployeePage(context.driver)
    context.manager_page = ManagerPage(context.driver)
    context.driver.implicitly_wait(4)

def after_all(context):
    context.driver.quit()