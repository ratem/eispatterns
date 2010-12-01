Feature: Path configuration
  As a Business Analyst
  I want to configure a path template
  In order to make it compliant to a given business process

  Scenario Outline: Path masking
    Given that I need to configure a path to reflect a given business process
    When I map path mask to <business process>
    Then the path mask should be <business process>

    Examples:
      | business process |
      | sale             |

  Scenario Outline: Movement inclusion
    Given that I want to include an already configured movement to a path
    When when I select a given <movement>
    Then this movement is included into the path

    Examples:
      | movement |
      | shipment |

