# Deleting a File:
# first need to import os module
# run os.remove() function.
"""
import os
os.remove("Ravi.txt")
"""

# To avoid getting error, check whether file exists before deleting it.

import os

if os.path.exists("Ravi.txt"):
    os.remove("Ravi.txt")
    print("file deleted")
else:
    print("File doesnot Exists")

