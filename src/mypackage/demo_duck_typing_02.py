import os
from pathlib import Path

from .demo_duck_typing import print_name

print_name(os)  # ok
print_name(Path.cwd())  # ok
print_name(1.23)  # error
