"""Tests for the main yourag module."""

import pytest
from yourag import main


def test_main_function_exists():
    """Test that the main function exists and is callable."""
    assert callable(main)


def test_main_function_runs():
    """Test that the main function runs without errors."""
    # Since main() prints to stdout, we can capture it
    import io
    import sys
    from contextlib import redirect_stdout

    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        main()

    output = captured_output.getvalue()
    assert "Hello from yourag!" in output


def test_main_function_output():
    """Test that the main function produces expected output."""
    import io
    import sys
    from contextlib import redirect_stdout

    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        main()

    output = captured_output.getvalue().strip()
    assert output == "Hello from yourag!"
