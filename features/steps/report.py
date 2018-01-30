from behave import *
from hathi_validate import result, report

use_step_matcher("re")


@given("we have a complete single Hathi package with 4 items, each with a txt, a jp2, and an xml with no errors")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """

    summary_builder = result.SummaryDirector(source="spam_source")
    context.summary = summary_builder.construct()


@when("I generate a report")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    context.string_report = report.get_report_as_str(context.summary, width=80)



@then("I should have a report that starts with a title header")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    lines = context.string_report.split("\n")


    # Top border line for the title
    assert lines[0] == "=" * 80

    assert lines[1] == "Validation Results"

    # Bottom border line for the title
    assert lines[2] == "=" * 80




@step("the report should have listed that No validation errors detected")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    lines = context.string_report.split("\n")
    assert lines[3] == "No validation errors detected."


@step("the report should close with a line")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    lines = context.string_report.split("\n")
    assert lines[-1] == "=" * 80


@given("we have a complete single Hathi package with 4 items, each with a txt and a jp2 but no xml")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    summary_builder = result.SummaryDirector(source="spam_source")
    summary_builder.add_error("Missing 0001.xml")
    summary_builder.add_error("Missing 0002.xml")
    summary_builder.add_error("Missing 0003.xml")
    summary_builder.add_error("Missing 0004.xml")
    context.summary = summary_builder.construct()


@step("the report should have a single source listed")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    lines = context.string_report.split("\n")
    assert lines[3] == "spam_source"


@step("that single source should have one error message stating it's missing the xml")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    report =context.string_report
    print(report)
    lines = report.split("\n")
    assert lines[5] == "* Missing 0001.xml"
    assert lines[6] == "* Missing 0002.xml"
    assert lines[7] == "* Missing 0003.xml"
    assert lines[8] == "* Missing 0004.xml"
