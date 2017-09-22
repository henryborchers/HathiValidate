import os

import sys
from cx_Freeze import setup, Executable
import pytest
import hathi_validate
import platform


def create_msi_tablename(python_name, fullname):
    shortname = python_name[:6].replace("_", "").upper()
    longname = fullname
    return "{}|{}".format(shortname, longname)


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
MSVC = os.path.join(PYTHON_INSTALL_DIR, 'vcruntime140.dll')


def get_tests():
    root = "tests"
    test_files = []
    for x in filter(lambda x: x.is_file and os.path.splitext(x.name)[1] == ".py", os.scandir(root)):
        test_files.append(os.path.join(root, x.name))
    print("Found files {}".format(", ".join(test_files)))
    return test_files


INCLUDE_FILES = [
    "documentation.url",
    #     TODO: BUILD DOCUMENTATION
] + get_tests()

directory_table = [
    (
        "ProgramMenuFolder",  # Directory
        "TARGETDIR",  # Directory_parent
        "PMenu|Programs",  # DefaultDir
    ),
    (
        "PMenu",  # Directory
        "ProgramMenuFolder",  # Directory_parent
        create_msi_tablename(hathi_validate.__title__, hathi_validate.FULL_TITLE)
    ),
]
shortcut_table = [
    (
        "startmenuShortcutDoc",  # Shortcut
        "PMenu",  # Directory_
        "{} Documentation".format(create_msi_tablename(hathi_validate.__title__, hathi_validate.FULL_TITLE)),
        "TARGETDIR",  # Component_
        "[TARGETDIR]documentation.url",  # Target
        None,  # Arguments
        None,  # Description
        None,  # Hotkey
        None,  # Icon
        None,  # IconIndex
        None,  # ShowCmd
        'TARGETDIR'  # WkDir
    ),
]

if os.path.exists(MSVC):
    INCLUDE_FILES.append(MSVC)

build_exe_options = {
    "includes": ["queue", "atexit", "appdirs", 'pkg_resources'] + pytest.freeze_includes(),
    "include_msvcr": True,
    "packages": ["os", "lxml", "packaging", "six", "appdirs", "hathi_validate"],
    "excludes": ["tkinter"],
    "include_files": INCLUDE_FILES,

}

target_name = "hathivalidate.exe" if platform.system() == "Windows" else "hathivalidate"
setup(
    name=hathi_validate.FULL_TITLE,
    description=hathi_validate.__description__,
    version=hathi_validate.__version__,
    author=hathi_validate.__author__,
    author_email=hathi_validate.__author_email__,
    options={
        "build_exe": build_exe_options,
        "bdist_msi": {
            "upgrade_code": "{9BCAE3C6-BF07-409A-9846-4C7BB474120A}",
            "data": {
                "Shortcut": shortcut_table,
                "Directory": directory_table
            }
        }
    },
    executables=[Executable("hathi_validate/cli.py",
                            targetName=target_name, base="Console")],

)
