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
      | '1234567-8'    | 10000,00      |

