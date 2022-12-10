Feature: MonsterIndia Job Application Update CV Profile

  Scenario: Updating CV Profile on "Monster India Website" Application
    Given launch the chrome browser
    When open monsterIndia.com homepage
#    And login with username "raneesseo@gmail.com" and password "possible2014" & updating Ranees CV on my profile page
    And login with username and password & updating Ranees CV on my profile page
    Then verify that it must be last updated on: current date
    Then logout the monsterIndia job profile
    Then close the browser
