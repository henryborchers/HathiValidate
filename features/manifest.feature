# Created by hborcher at 1/30/2018
Feature: Create a package manifest report
  # Enter feature description here

  Scenario: Manifest report for a single package
    Given we have a complete single Hathi package including a checksum, marc xml, and a meta yml with 2 items, each with a txt, a jp2, and an xml
    When I generate a manifest report
    Then I should have a manifest report that starts with a title header
    And the manifest report should state package path contains 2 .txt , 2 .jp2, and 2 .xml files
    And the report should close with a line

  Scenario: Manifest report for a three packages
    Given we have a complete three Hathi packages, the first one has 3 files, the second one has 2 files, and the third one has 4 files
    When I generate a manifest report
    Then I should have a manifest report that starts with a title header
    And the manifest report should state 3 packages with their file components
    And the report should close with a line