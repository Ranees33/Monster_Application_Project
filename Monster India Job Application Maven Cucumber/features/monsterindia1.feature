Feature: MonsterIndia Job Application Login

  Scenario: Login with Credentials on "Monster India Website" Application
    Given launch chrome browser
    When open MonsterIndia homepage
    When login the application with username "raneesseo@gmail.com" and password "possible2014"
    Then verify that the redirect to profile page
    And close browser
