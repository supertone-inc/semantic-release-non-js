import sys
from setuptools import setup

__version__ = "0.1.0"

setup(
   name="semantic-release-non-js",
   version=__version__,
   # And so on...
)

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass
