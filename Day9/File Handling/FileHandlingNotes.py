# File Handling:
# Means the process of dealing with files
# like performing operations like reading, writing, deleting files.

# Several Programming Languages have the concept of file handling and its implementation
# is little complicated

# But in python, it is easy due to inbuilt functions

# python treats files int 2 ways: text and binary(e.g images)

# Text file: Each line contains sequence of characters and they form a file

# EOL: Each line in a file is terminatied by EOL (End of Line) which is generally
# a newline Character

# ADVANATGES OF FILE HANDLING:
# 1. It allows to perform many operations like creating, reading, writing, deleting, etc
# 2. Python provides a user-friendly interface for file handling
# 3. platform independent: file handling can work across different platforms(windows,linux,etc)

# DISADVANTAGES:
# 1. Can cause a lot of errors when the code is not written carefully
# 2. Can cause security risks in case of modifying sensitive or confidential files on system.

# First Step: opening the file

# open() function:
# It is the key inbuilt function for handling files.
# Takes two parameters: filename, mode
# Syntax:
# file = open(filename, mode)

# TYPES OF MODES FOR OPENING FILE:
# 1. "r" : (Default Mode) Opens an existing file for Reading. Display Error if file not exist
# 2. "a" : Opens an existing file for Appending. Creates a new file if not exist. It won't override
#          the existing data.
# 3. "w" : Opens an existing fil3 for writing. Creates a new file if not exists. If the file already
#          contains some data, it will be overridden
# 4. "x" : creates a new file. Error if the file already exists.
# 5. "t" : (Default) for handling file in text mode
# 6. "b" : for handling file in Binary mode(e.g images)





