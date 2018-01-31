# Created by hborcher at 1/30/2018
Feature: Report generator
  # Enter feature description here

  Scenario: Report for a package with no bad data
    Given we have a complete single Hathi package with 4 items, each with a txt, a jp2, and an xml with no errors
    When I generate a report
    Then I should have a report that starts with a title header
    And the report should have listed that No validation errors detected
    And the report should close with a line

  Scenario: Report for a package with one bad item
    Given we have a complete single Hathi package with 4 items, each with a txt and a jp2 but no xml
    When I generate a report
    Then I should have a report that starts with a title header
    And the report should have a single source listed
    And that single source should have one error message stating it's missing the xml
    And the report should close with a line