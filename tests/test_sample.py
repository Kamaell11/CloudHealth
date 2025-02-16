import pytest


def test_addition():
    assert 1 + 1 == 2


def test_string_contains():
    sample_string = "Hello, World!"
    assert "World" in sample_string


def test_raises_error():
    with pytest.raises(ZeroDivisionError):
        1 / 0
