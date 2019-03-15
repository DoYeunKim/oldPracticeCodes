# input([prompt])
# Assumes that the input is a valid Python expression

# Opening a file
# file object = open(file_name [, access_mode][, buffering])
""" access_mode
    r: reading only (default)
    rb: read only in bin (default)
    r+: reading & writing
    rb+: r+ in bin
    w: writing only (overwrites if already there, newly creates if not)
    wb: w in bin
    w+: same as r+ but w/ file modification of w
    wb+: w+ in bin
    a: appending (w+ but starting at the end)
    ab: a in bin
    a+: appending & reading
    ab+: a+ in bin
"""

# attribute & description
"""
    file.closed: bool whether file is closed
    file.mode: return access mode
    file.name: name
"""

#e.g.
fo = open("foo.txt", "w")
print("Name of the file:", fo.name)
print("Closed?:", fo.closed)
print("Opening mode:", fo.mode)
fo.write("Python is easy'\n'..ish")
fo.close()

fo = open("foo.txt", "r+")
str = fo.read(10) #count = numBytes (default max)
print("Read String is:", str)
# tell(): current position
position = fo.tell()
print("Current file position:", position)
#seek(offset [, from]): changes current file position (numBytes)
position = fo.seek(0,0)
str = fo.read(10)
print("Again read string is:", str)
fo.close

# os.rename(curr_file_name, new_file_name)
import os

os.rename("foo.txt", "foo_py.txt")

os.remove("foo_py.txt")

"""
    Familiar commands...
    os.mkdir()
    os.getcwd()
    os.rmdir()
"""