import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Files you want to create, relative to current directory
list_of_files = [
    "tavily/__init__.py",
    "tavily/example.py",
    "setup.py",
    "README.md",
]

for filepath_str in list_of_files:
    filepath = Path(filepath_str)
    filedir = filepath.parent  # directory part

    if filedir != Path('.'):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Ensured directory exists: {filedir}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass  # create empty file
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")
