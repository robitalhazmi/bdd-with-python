Feature: Search

  Scenario: Search User
    Given I navigate to the Twitter Search page
    When I search for "Robit Alhazmi"
    Then I am taken to Twitter Search Results page
    And I see a search result "Robit Alhazmi"