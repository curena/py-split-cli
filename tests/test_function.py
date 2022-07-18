"""Test cli_app functions."""

from cli_app import app


def test_app():
    """Test app.main function."""
    assert app.main("ah ", 3) == "ah ah ah "
