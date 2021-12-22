Feature: User logout feature
  Scenario: as an employee I should be able to logout
    Given the employee is on the employee page
    When the user clicks on sign out
    Then the user should be redirected to the home page


  Scenario: as a manager I should be able to logout
    Given the manager is on the manager page
    When the user clicks on sign out
    Then the user should be redirected to the home page

