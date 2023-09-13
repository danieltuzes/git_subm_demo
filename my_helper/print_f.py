"""Minimal repo with dependency on numpy."""

import sys
import pandas

__version__ = "1.0.6"


def my_print_f():
    """Print diagnostics."""
    print(f"My helper's print file is at {__file__}, version {__version__}")
    print(f"pandas version {pandas.__version__}")
    print(f"sys.argv = {sys.argv}")
    print(f"sys.path = {sys.path}")
