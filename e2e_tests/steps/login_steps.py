from behave import Given, When, Then
import time


@Given(u'the user is on the home page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Ozgur/Desktop/repo/project1web/index.html")

@When(u'the user enters the username styphon')
def step_impl(context):
    context.index_page.select_username_input().send_keys("styphon")


@When(u'the user enters the password 1234')
def step_impl(context):
    context.index_page.select_password_input().send_keys("1234")

@When(u'the user clicks sign in')
def step_impl(context):
    context.index_page.select_sign_in_button().click()



@Then(u'the employee should be redirected to the employee page')
def step_impl(context):
    time.sleep(1)
    assert context.driver.title == "Employee Page"

@When(u'the user enters the username styphon31')
def step_impl(context):
    context.index_page.select_username_input().send_keys("styphon31")


@When(u'the user enters the password 4321')
def step_impl(context):
    context.index_page.select_password_input().send_keys("4321")

@Then(u'the manager should be redirected to the manager page')
def step_impl(context):
    time.sleep(1)
    assert context.driver.title == "Manager Page"

@When(u'the user enters the password 5432')
def step_impl(context):
    context.index_page.select_password_input().send_keys("5432")


@Then(u'the user should get invalid credentials error')
def step_impl(context):
    time.sleep(1)
    assert context.driver.switch_to.alert.text == "Invalid credentials"
    context.driver.switch_to.alert.accept()


@When(u'the user enters the username asda')
def step_impl(context):
    context.index_page.select_username_input().send_keys("asda")

@When(u'the user enters the username asdasda')
def step_impl(context):
    context.index_page.select_username_input().send_keys("asdasda")


@When(u'the user enters the password aasdas')
def step_impl(context):
    context.index_page.select_password_input().send_keys("aasdas")
