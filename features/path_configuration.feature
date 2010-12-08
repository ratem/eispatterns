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
    Given there is a configured <path> available
    And I want to include a configured movement to this path
    When I select a given <movement>
    And I include this movement into the path
    Then this movement should be into the path

    Examples:
      | path | movement |
      | sale | shipment |

  Scenario Outline: Connection inclusion
    Given there is a configured <path> available
    And this <path> has at least two movements
    And there is at least a connection which integrates two of these movements
    When I select a given <connection> to be included
    Then this connection should be included into the path

    Examples:
      | path | connection                        |
      | sale | Payment is condition for Shipment |

