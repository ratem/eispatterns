Feature: Connection configuration
  As a Business Analyst
  I want to configure a concrete connection of movements
  In order to make it usefull for using in paths

  Scenario Outline: Connection configuration
    Given I need to configure a connection as a <new type of connection>
    When I map left hand to <left hand movement>
    And I map right hand to <right hand movement>
    And I map binding type to <binding type>
    And I map binding time to <binding time>
    Then the connection mask should be <new type of connection>
    And new connection's left hand should be of <left hand movement>
    And new connection's right hand type should be of <right hand movement>
    And new connection's binding type should be of <binding type>
    And new connection's binding time should be <binding time>

    Examples:
      | new type of connection            | left hand movement | right hand movement | binding type    | binding time    |
      | Payment is condition for Shipment | payment            | shipment            | triggers before | event dependent |

