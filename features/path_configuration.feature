Feature: Path configuration
  As a Business Analyst
  I want to configure a path template
  In order to make it compliant to a given business process

  Scenario Outline: Path masking
    Given I need to configure a path to reflect a given business process
    When I map path mask to <business process>
    Then the path mask should be <business process>

    Examples:
      | business process |
      | sale             |

  Scenario Outline: Movement inclusion
    Given I have a configured <path>
    And I want to include a configured movement to this path
    When I select a given <movement>
    And I include this movement into the path
    Then this movement should be into the path

    Examples:
      | path | movement |
      | sale | shipment |

