Feature: The manager should be able to manage reimbursements

  Scenario Outline: as a manager, I should be able to approve reimbursement requests
    Given the manager is on the manager page
    When the manager clicks a pending reimbursement
    When the manager enters status <status>
    When the manager enters reject reason <reject_reason>
    When the manager clicks save changes
    Then the reimbursement should be approved

    Examples:
      | status | reject_reason |
      | accept | -             |

  Scenario Outline: as a manager, I should be able to reject reimbursement requests
    Given the manager is on the manager page
    When the manager clicks a pending reimbursement
    When the manager enters status <status>
    When the manager enters reject reason <reject_reason>
    When the manager clicks save changes
    Then the reimbursement should be rejected

    Examples:
      | status | reject_reason |
      | reject | I am in a bad mood |

  Scenario: as a manager, I should be able to view pending reimbursements
    Given the manager is on the manager page
    When the manager clicks pending reimbursement
    Then the manager should be able to see pending reimbursements


  Scenario: as a manager, I should be able to view rejected reimbursements
    Given the manager is on the manager page
    When the manager clicks rejected reimbursement
    Then the manager should be able to see rejected reimbursements

  Scenario: as a manager, I should be able to view accepted reimbursements
    Given the manager is on the manager page
    When the manager clicks accepted reimbursement
    Then the manager should be able to see accepted reimbursements

  Scenario: as a manager, I should be able to view reimbursements stats
    Given the manager is on the manager page
    Then the manager should be able to see stats