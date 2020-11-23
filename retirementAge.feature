Feature: Get retirement age
  I want to know my retirement age

  Scenario Outline: Find retirement age
    Given fullRetirementAge has been started in the terminal
    When my year of birth is entered
    And my birth month is entered
    Then my retirement age is displayed
    Examples: