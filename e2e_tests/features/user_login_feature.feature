Feature: The user should be able to login securely

  Scenario Outline: as an employee I should be able to login so I can manage my reimbursements
    Given the user is on the home page
    When the user enters the username <username>
    When the user enters the password <password>
    When the user clicks sign in
    Then the employee should be redirected to the employee page

    Examples:
      | username | password |
      | styphon  | 1234     |


    Scenario Outline: as a manager I should be able to login so I can manage my reimbursements
    Given the user is on the home page
    When the user enters the username <username>
    When the user enters the password <password>
    When the user clicks sign in
    Then the manager should be redirected to the manager page

    Examples:
      | username  | password |
      | styphon31 | 4321     |

    Scenario Outline: as system I should reject failed login attempts
    Given the user is on the home page
    When the user enters the username <username>
    When the user enters the password <password>
    When the user clicks sign in
    Then the user should get invalid credentials error

    Examples:
      | username  | password |
      | styphon31 | 5432     |
      | asda      | 4321     |
      | styphon   | 5432     |
      | asda      | 1234     |
      | asdasda   | aasdas   |
