from behave import Given, When, Then
import time

@When(u'the user clicks on sign out')
def step_impl(context):
    context.employee_page.select_sign_out_button().click()
    time.sleep(1)


@Then(u'the user should be redirected to the home page')
def step_impl(context):
    assert context.driver.title == "Project1"
