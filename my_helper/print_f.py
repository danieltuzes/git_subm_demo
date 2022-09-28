"""Minimal repo with dependency on numpy."""

import numpy

__version__="1.0.3"

def my_pr_f():
    """Prints versions."""
    print("You have my_helper version", __version__)
    print("You have numpy version", numpy.__version__)
