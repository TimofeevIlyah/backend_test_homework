import os
from pathlib import  Path

os.makedirs('path/to/directory', exist_ok=True)
Path('path/to/folder').mkdir(parents=True, exist_ok=True)

# with open('path/to/folder/test.txt', 'w')
