from behave import Given, When, Then
import time

@Given(u'the employee is on the employee page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Ozgur/Desktop/repo/project1web/index.html")
    context.index_page.select_username_input().send_keys("styphon")
    context.index_page.select_password_input().send_keys("1234")
    context.index_page.select_sign_in_button().click()
    time.sleep(1)
    assert context.driver.title == "Employee Page"


@When(u'the employee click new reimbursement button')
def step_impl(context):
    context.employee_page.select_create_reimbursement_button().click()


@When(u'the employee enters expense name E2E Test')
def step_impl(context):
    time.sleep(1)
    context.employee_page.select_expense_name_input().send_keys("E2E Test")


@When(u'the employee enters expense amount 20.5')
def step_impl(context):
    context.employee_page.select_expense_amount_input().send_keys("20.5")

@When(u'the employee enters expense reason I was hungry')
def step_impl(context):
    context.employee_page.select_expense_reason_input().send_keys("I was hungry")


@When(u'the employee clicks save changes')
def step_impl(context):
    context.employee_page.select_save_button().click()


@Then(u'then a new reimbursement should be created')
def step_impl(context):
    time.sleep(1)
    assert context.employee_page.select_created_reimbursement() is not None


@When(u'the employee enters expense amount -5')
def step_impl(context):
    context.employee_page.select_expense_amount_input().send_keys("-5")


@Then(u'the employee should be alerted a warning')
def step_impl(context):
    assert context.driver.switch_to.alert.text == "Expense Amount must be a positive number"
    context.driver.switch_to.alert.accept()

@When(u'the employee enters expense amount e')
def step_impl(context):
    context.employee_page.select_expense_amount_input().send_keys("e")


@Then(u'then the employee should be able to see reimbursements')
def step_impl(context):
    assert context.employee_page.select_created_reimbursement() is not None
    context.employee_page.select_created_reimbursement().click




