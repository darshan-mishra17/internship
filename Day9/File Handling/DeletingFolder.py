# Need to import os module first
# need to run os.rmdir() function : deletes the entire folder

"""
import os
os.rmdir("demo")
"""

# Only Empty Folders can be removed

# To avoid getting error, check whether file exists before deleting it.

import os
if os.path.exists("demo"):
    os.rmdir("demo")
    print("folder deleted")
else:
    print("File doesnot Exists")

