Feature: Individual Customer Credit Operation
  As a Credit Analyst
  I want to process a loan request from an individual customer
  In order to approve or not the loan

  Scenario Outline: Individual Customer asks for loan
    Given I am a registered Credit Analyst
    And an individual customer with account number <account number> asks for a personal loan
    And the loan request is of <desired value>
    When I confirm the loan request
    Then a new loan request with the <account number> and <desired value> is created
    And the new loan request is associated to the Credit Analyst

    Examples:
      | account number | desired value |
      | 1234567-8      | 10000,00      |

  Scenario Outline: Credit Analyst analyses the individual customer loan request
    Given I am a registered Credit Analyst
    And there is a loan request of account <account number> to be analysed
    When I pick to analyse the loan request of account <account number>
    Then the loan request has the decision <decision>

    Examples:
      | account number | desired value | decision |
      | 1234567-8      | 10000,00      | False    |

  Scenario Outline: Approved loan request
    Given a loan request of value <value> for account <account number> was approved
    When When I pick and perfom this loan
    Then a loan of value <value> for account <account number> is generated
    And the loan_request is moved to the account <account number> historic

    Examples:
      | account number | desired value |
      | 0987654-3      | 500,00        |

