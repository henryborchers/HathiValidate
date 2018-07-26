import pytest
import hathi_validate


def test_get_alto():
    alto = hathi_validate.get_scheme("alto")
    assert isinstance(alto, bytes)
    lines = alto.decode().split("\n")
    lines[0].startswith('<?xml version="1.0" encoding="UTF-8"?>\n<!-- ALTO: Analyzed Layout and Text Object  -->')


def test_get_bad_scheme():
    with pytest.raises(ValueError):
        bad = hathi_validate.get_scheme("BAD")