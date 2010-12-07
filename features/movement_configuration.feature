Feature: Movement configuration
  As a Business Analyst
  I want to configure a concrete movement
  In order to make it usefull for using in paths

  Scenario Outline: Movement configuration
    Given I need to configure a movement as a <new concept>
    When I map movement source to <source type>
    And I map movement destination to <destination type>
    And I map movement resource to <resource type>
    And I map movement quantity to <quantity type>
    Then the movement mask should be <new concept>
    And new concept's source type should be of <source type>
    And new concept's destination type should be of <destination type>
    And new concept's resource type should be of <resource type>
    And new concept's quantity type should be <quantity type>

    Examples:
      | new concept | source type | destination type | resource type | quantity type |
      | shipment    | inventory   | shipment bay     | container     | integer       |

