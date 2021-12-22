from behave import Given, When, Then
import time


@Given(u'the manager is on the manager page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Ozgur/Desktop/repo/project1web/index.html")
    context.index_page.select_username_input().send_keys("styphon31")
    context.index_page.select_password_input().send_keys("4321")
    context.index_page.select_sign_in_button().click()
    time.sleep(1)
    assert context.driver.title == "Manager Page"


@When(u'the manager clicks a pending reimbursement')
def step_impl(context):
    context.manager_page.select_a_pending_reimbursement().click()
    time.sleep(1)

@When(u'the manager enters status accept')
def step_impl(context):
    context.manager_page.select_status_dropdown().select_by_visible_text('Accept')


@When(u'the manager enters reject reason -')
def step_impl(context):
    context.manager_page.select_reason_input().send_keys("-")

@When(u'the manager clicks save changes')
def step_impl(context):
    context.manager_page.select_save_button().click()
    time.sleep(1)

@Then(u'the reimbursement should be approved')
def step_impl(context):
    context.manager_page.select_accepted_reimbursement_button().click()
    time.sleep(1)
    context.manager_page.select_last_reimbursement().click()
    time.sleep(1)
    assert context.manager_page.select_last_reimbursement_reason().text == "Reject Reason: -"



@When(u'the manager enters status reject')
def step_impl(context):
    context.manager_page.select_status_dropdown().select_by_visible_text('Reject')

@When(u'the manager enters reject reason I am in a bad mood')
def step_impl(context):

    context.manager_page.select_reason_input().send_keys("I am in a bad mood")


@Then(u'the reimbursement should be rejected')
def step_impl(context):
    context.manager_page.select_rejected_reimbursement_button().click()
    time.sleep(1)
    context.manager_page.select_last_reimbursement().click()
    time.sleep(1)
    assert context.manager_page.select_last_reimbursement_reason().text == "Reject Reason: I am in a bad mood"


@When(u'the manager clicks pending reimbursement')
def step_impl(context):
    context.manager_page.select_pending_reimbursement_button().click()
    time.sleep(1)


@Then(u'the manager should be able to see pending reimbursements')
def step_impl(context):

    assert context.manager_page.select_last_reimbursement_status().text == "pending"



@When(u'the manager clicks rejected reimbursement')
def step_impl(context):
    context.manager_page.select_rejected_reimbursement_button().click()
    time.sleep(1)


@Then(u'the manager should be able to see rejected reimbursements')
def step_impl(context):
    assert context.manager_page.select_last_reimbursement_status().text == "rejected"


@When(u'the manager clicks accepted reimbursement')
def step_impl(context):
    context.manager_page.select_accepted_reimbursement_button().click()
    time.sleep(1)


@Then(u'the manager should be able to see accepted reimbursements')
def step_impl(context):
    assert context.manager_page.select_last_reimbursement_status().text == "accepted"

@Then(u'the manager should be able to see stats')
def step_impl(context):
    assert context.manager_page.select_stats() is not None
