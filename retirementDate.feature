Feature: Get retirement date
  I want to know my retirement date
  
  Scenario: Find retirement date
    Given fullRetirementAge has been started in the terminal
    When my year of birth is entered
	And my birth month is entered
    Then my retirement date is displayed