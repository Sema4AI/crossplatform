import pytest
from sema4ai.crossplatform import trigger_excel_save_on_app
from sema4ai.crossplatform._win import _trigger_excel_on_windows
from sema4ai.crossplatform._mac import _trigger_excel_on_mac
import logging
import platform

logger = logging.getLogger(__name__)

# Common test variables
EXCEL_FILE_SIMPLE = "./tests/resources/simple.xlsx"


def test_excel_launch_on_windows():
    """Fixture for common Excel parameters"""
    result = _trigger_excel_on_windows(EXCEL_FILE_SIMPLE)
    if platform.system() == "Windows":
        assert result
    else:
        assert not result


def test_excel_launch_on_mac():
    """Fixture for common Excel parameters"""
    result = _trigger_excel_on_mac(EXCEL_FILE_SIMPLE)
    if platform.system() == "Darwin":
        assert result
    else:
        assert not result
