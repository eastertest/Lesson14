Feature: Exit fullRetirementAge
  I want to exit the program instead of getting my results
  
  Scenario: User wants to exit
    Given fullRetirementAge has been started in the terminal
    When Only the enter key is pressed
    Then fullRetirementAge exits