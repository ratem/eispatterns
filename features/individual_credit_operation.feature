Feature: Individual Customer Credit Operation
  As a Credit Analyst
  I want to process a loan request from an individual customer
  In order to approve or not the loan

  Scenario Outline: Individual Customer asks for loan
    Given I am a registered Credit Analyst with number <analyst number>
    And an individual customer asks for a personal loan
    And the customer's account number is <account number>
    And the customer's asks for a personal loan of <desired value>
    When I confirm the loan request
    Then a new loan request with the <account number>, <desired value>, and <analyst number> is created

    Examples:
      | analyst number | account number | desired value |
      | '09876-5'      | '1234567-8'    | 10000,00      |

