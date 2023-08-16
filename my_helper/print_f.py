"""Minimal repo with dependency on numpy."""

import sys
import numpy

__version__="1.0.5"

def my_print_f():
    """Print diagnostics."""
    print(f"My helper's print file is at {__file__}, version {__version__}")
    print(f"numpy version {numpy.__version__}")
    print(f"sys.argv = {sys.argv}")
    print(f"sys.path = {sys.path}")