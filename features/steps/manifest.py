from behave import *
import hathi_validate.manifest

use_step_matcher("re")


@given(
    "we have a complete single Hathi package including a checksum, marc xml, and a meta yml with 2 items, each with a txt, a jp2, and an xml")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    manifest_director = hathi_validate.manifest.PackageManifestDirector()
    package = manifest_director.add_package("./dummy/0001")

    package.add_file("00001.xml")
    package.add_file("00001.jp2")
    package.add_file("00001.txt")

    package.add_file("00002.xml")
    package.add_file("00002.jp2")
    package.add_file("00002.txt")

    package.add_file("checksum.md5")
    package.add_file("meta.yml")
    package.add_file("marc.xml")

    manifest = manifest_director.build_manifest()
    context.manifest = manifest


@when("I generate a manifest report")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    context.string_report = hathi_validate.manifest.get_report_as_str(context.manifest, width=80)


@then("I should have a manifest report that starts with a title header")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    lines = context.string_report.split("\n")

    # Top border line for the title
    assert lines[0] == "=" * 80

    assert lines[1] == "Manifest"

    # Bottom border line for the title
    assert lines[2] == "=" * 80


@step("the manifest report should state package path contains 2 \.txt , 2 \.jp2, and 2 \.xml files")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    lines = context.string_report.split("\n")
    assert lines[4] == "./dummy/0001"
    assert lines[5] == " * .jp2: 2 file(s)"
    assert lines[6] == " * .md5: 1 file(s)"
    assert lines[7] == " * .txt: 2 file(s)"
    assert lines[8] == " * .xml: 3 file(s)"
    assert lines[9] == " * .yml: 1 file(s)"


@given(
    "we have a complete three Hathi packages, the first one has 3 files, the second one has 2 files, and the third one has 4 files")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """
    manifest_director = hathi_validate.manifest.PackageManifestDirector()

    # First package
    package = manifest_director.add_package("./dummy/0001")

    package.add_file("00001.xml")
    package.add_file("00001.jp2")
    package.add_file("00001.txt")

    package.add_file("00002.xml")
    package.add_file("00002.jp2")
    package.add_file("00002.txt")

    package.add_file("00003.xml")
    package.add_file("00003.jp2")
    package.add_file("00003.txt")

    package.add_file("checksum.md5")
    package.add_file("meta.yml")
    package.add_file("marc.xml")

    # second package
    package = manifest_director.add_package("./dummy/0002")

    package.add_file("00001.xml")
    package.add_file("00001.jp2")
    package.add_file("00001.txt")

    package.add_file("00002.xml")
    package.add_file("00002.jp2")
    package.add_file("00002.txt")

    package.add_file("checksum.md5")
    package.add_file("meta.yml")
    package.add_file("marc.xml")

        # First package
    package = manifest_director.add_package("./dummy/0003")

    package.add_file("00001.xml")
    package.add_file("00001.jp2")
    package.add_file("00001.txt")

    package.add_file("00002.xml")
    package.add_file("00002.jp2")
    package.add_file("00002.txt")

    package.add_file("00003.xml")
    package.add_file("00003.jp2")
    package.add_file("00003.txt")

    package.add_file("00004.xml")
    package.add_file("00004.jp2")
    package.add_file("00004.txt")

    package.add_file("checksum.md5")
    package.add_file("meta.yml")
    package.add_file("marc.xml")


    manifest = manifest_director.build_manifest()
    context.manifest = manifest


@step("the manifest report should state 3 packages with their file components")
def step_impl(context):
    """
    Args:
        context (behave.runner.Context):
    """

    lines = context.string_report.split("\n")

    assert lines[4] == "./dummy/0001"
    assert lines[5] == " * .jp2: 3 file(s)"
    assert lines[6] == " * .md5: 1 file(s)"
    assert lines[7] == " * .txt: 3 file(s)"
    assert lines[8] == " * .xml: 4 file(s)"
    assert lines[9] == " * .yml: 1 file(s)"

    assert lines[11] == "./dummy/0002"
    assert lines[12] == " * .jp2: 2 file(s)"
    assert lines[13] == " * .md5: 1 file(s)"
    assert lines[14] == " * .txt: 2 file(s)"
    assert lines[15] == " * .xml: 3 file(s)"
    assert lines[16] == " * .yml: 1 file(s)"

    assert lines[18] == "./dummy/0003"
    assert lines[19] == " * .jp2: 4 file(s)"
    assert lines[20] == " * .md5: 1 file(s)"
    assert lines[21] == " * .txt: 4 file(s)"
    assert lines[22] == " * .xml: 5 file(s)"
    assert lines[23] == " * .yml: 1 file(s)"

    print(context.string_report)
