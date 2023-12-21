# creating folder
# use os.mkdir() function
"""
import os
os.mkdir("demo")
"""

# To avoid getting error, check whether file exists before deleting it.

import os
if not os.path.exists("demo"):
    os.mkdir("demo")
    print("folder created")
else:
    print("Folder Already Exists")