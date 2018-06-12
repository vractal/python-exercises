#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    dir = os.path.abspath(dir)
    paths = []
    for file in os.listdir(dir):
        if re.match(r'.*__[^_]*__.*',file):
            paths.append(os.path.join(dir,file))

    return paths

def copy_to(paths,dir):
    dir = os.path.abspath(dir)
    if not os.path.exists(dir):
        os.makedirs(dir)
    for path in paths:
        shutil.copy(path,dir)
    return True


def zip_to(paths, zip):
    command = "zip -j " + zip
    for path in paths:
        command += " " + path
    subprocess.call(command,shell=True)







def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ""
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ""
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

        # +++your code here+++
        # Call your functions

    special_paths = []
    for arg in args:
        special_paths += get_special_paths(arg)

    if todir:
        copy_to(special_paths,todir)
    elif tozip:
        zip_to(special_paths,tozip)
    else:
        print(special_paths)





if __name__ == "__main__":
    main()
