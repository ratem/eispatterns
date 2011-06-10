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
      | 1234567-8      | 10000         |

  Scenario Outline: Credit Analyst analyses the individual customer loan request
    Given I am a registered Credit Analyst
    And there is a loan request of account <account number> with desired value <desired value> to be analysed
    When I pick to analyse the loan request of account <account number>
    Then the loan request for account <account number> has the decision <decision>

    Examples:
      | account number | desired value | decision |
      | 1234567-8      | 10000         | True     |

  Scenario Outline: Approved loan request
    Given I am a registered Credit Analyst
    And there is an approved loan request of value <value> for account <account number>
    When I ask for performing this loan
    Then a loan of value <value> for account <account number> is generated
    And the value is moved to the account <account number>
    And the loan is moved to the account <account number> historic

    Examples:
      | account number | desired value |
      | 0987654-3      | 10000         |

  Scenario Outline: Refused loan request
    Given I am a registered Credit Analyst
    And there is a refused loan request of value <desired value> for account <account number>
    When I pick this loan request
    Then the loan_request is moved to the account <account number> historic
    And an refusal letter is sent to the account holder

    Examples:
      | account number | desired value |
      | 0987654-3      | 10005         |

