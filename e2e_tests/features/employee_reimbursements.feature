Feature: The employee should be able to manage reimbursements

  Scenario Outline: I should be able to submit new reimbursement requests
    Given the employee is on the employee page
    When the employee click new reimbursement button
    When the employee enters expense name <expense_name>
    When the employee enters expense amount <expense_amount>
    When the employee enters expense reason <expense_reason>
    When the employee clicks save changes
    Then then a new reimbursement should be created

    Examples:
      | expense_name | expense_amount | expense_reason |
      | E2E Test     | 20.5           | I was hungry   |

  Scenario Outline: as the system, I should reject negative values for reimbursement requests
    Given the employee is on the employee page
    When the employee click new reimbursement button
    When the employee enters expense name <expense_name>
    When the employee enters expense amount <expense_amount>
    When the employee enters expense reason <expense_reason>
    When the employee clicks save changes
    Then the employee should be alerted a warning

    Examples:
      | expense_name | expense_amount | expense_reason |
      | E2E Test         | -5             | I was hungry   |

  Scenario Outline: as the system, I should reject non-numeric for reimbursement requests
    Given the employee is on the employee page
    When the employee click new reimbursement button
    When the employee enters expense name <expense_name>
    When the employee enters expense amount <expense_amount>
    When the employee enters expense reason <expense_reason>
    When the employee clicks save changes
    Then the employee should be alerted a warning

    Examples:
      | expense_name | expense_amount | expense_reason |
      | E2E Test           | e              | I was hungry   |

  Scenario: I should be able to review my reimbursement requests so I can know if they are approved or denied
    Given the employee is on the employee page
    Then then the employee should be able to see reimbursements


