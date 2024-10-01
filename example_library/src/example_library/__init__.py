from importlib import metadata
import os

from .domain_logic import *

os.chdir(os.path.dirname(__file__))

__title__ = __name__
__version__ = metadata.version(__title__)
