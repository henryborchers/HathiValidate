import os
import sys
import pytest
from hathi_validate import package

WINDOWS_ROOT = "c:/my_hathi_package"
UNIX_ROOT = "/my_hathi_package"
ROOT = WINDOWS_ROOT if sys.platform == "win32" else UNIX_ROOT

class mockDirEntry:
    def __init__(self, name, source, is_dir):
        self.name = name
        self.path = os.path.join(source, name)
        self._is_dir = is_dir

    def is_dir(self):
        return self._is_dir


@pytest.fixture()
def sample_hathi_package(monkeypatch):
    def mockreturn(path):
        return [
            mockDirEntry(name="00000001.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000001.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000002.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000002.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000003.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000003.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000004.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000004.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000005.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000005.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000006.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000006.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000007.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000007.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000008.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000008.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000009.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000009.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000010.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000010.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000011.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000011.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000012.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000012.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000013.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000013.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000014.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000014.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000015.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000015.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000016.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000016.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000017.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000017.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000018.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000018.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000019.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000019.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000020.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000020.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000021.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000021.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000022.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000022.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000023.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000023.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000024.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000024.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000025.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000025.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000026.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000026.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000027.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000027.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000028.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000028.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000029.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000029.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000030.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000030.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000031.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000031.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000032.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000032.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000033.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000033.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000034.jp2", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="00000034.txt", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="checksum.md5", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="marc.xml", source=os.path.join(ROOT, "721932"), is_dir=False),
            mockDirEntry(name="meta.yml", source=os.path.join(ROOT, "721932"), is_dir=False),
        ]

    monkeypatch.setattr(os, "scandir", mockreturn)


@pytest.fixture()
def sample_hathi_package_folder(monkeypatch):

    def mockreturn(path):
        return [
            mockDirEntry(name="2693684", source=ROOT, is_dir=True),
            mockDirEntry(name="2942435", source=ROOT, is_dir=True),
            mockDirEntry(name="6852190", source=ROOT, is_dir=True),
            mockDirEntry(name="7213538", source=ROOT, is_dir=True),
            mockDirEntry(name="7213857", source=ROOT, is_dir=True),
            mockDirEntry(name="7213932", source=ROOT, is_dir=True),
            mockDirEntry(name="7214043", source=ROOT, is_dir=True),
            mockDirEntry(name="7215655", source=ROOT, is_dir=True),
            mockDirEntry(name="7215682", source=ROOT, is_dir=True),
            mockDirEntry(name="7215700", source=ROOT, is_dir=True),
            mockDirEntry(name="7465982", source=ROOT, is_dir=True),
            mockDirEntry(name="8102529", source=ROOT, is_dir=True),

            ]


    monkeypatch.setattr(os, "scandir", mockreturn)


def test_get_folders(sample_hathi_package_folder):
    expected_paths =[
        os.path.join(ROOT, "2693684"),
        os.path.join(ROOT, "2942435"),
        os.path.join(ROOT, "6852190"),
        os.path.join(ROOT, "7213538"),
        os.path.join(ROOT, "7213857"),
        os.path.join(ROOT, "7213932"),
        os.path.join(ROOT, "7214043"),
        os.path.join(ROOT, "7215655"),
        os.path.join(ROOT, "7215682"),
        os.path.join(ROOT, "7215700"),
        os.path.join(ROOT, "7465982"),
        os.path.join(ROOT, "8102529"),
    ]

    for x in package.get_dirs(WINDOWS_ROOT):
        assert x in expected_paths
