Feature: Search

  Scenario: Top Search
    Given I navigate to the Twitter Search page
    When I search for "Robit Alhazmi"
    Then I am taken to Twitter Search Results page

  Scenario: Search User
    Given Top search results for "Robit Alhazmi" are shown
    When I click on the "People" link
    Then User related to "Robit Alhazmi" are shown on the results page