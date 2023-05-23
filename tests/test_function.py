"""Test cli_app functions."""

# add parent directory to path
import pytest
from typer.testing import CliRunner
from cli_app import app

def test_app():
    test_app = CliRunner()
    result = test_app.invoke(app.app, ["hello", "cecill"])
    assert result.exit_code == 0
    assert "Hello, cecill!\n" in result.stdout
    
