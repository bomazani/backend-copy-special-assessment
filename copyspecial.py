#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise
"""


def get_special_paths(dir):
    spec_paths = []
    ### returns a list of the absolute paths of the special files in the given directory ###
    for root, dirs, files in os.walk("."):  
        for filename in files:
            if re.search(r'\__\w*\__', filename):
                print('*Special* ' + filename)
    return


def copy_to(paths, dir):
    ### given a list of paths, copies those files into the given directory ###
    pass


def zip_to(paths, zippath):
    ### given a list of paths, zip those files up into the given zipfile ###
    pass


def create_parser():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument(
        '-d', '--dir', help='directory of files to search', default='.')
    return parser

# Write functions and modify main() to call them


def main(args):
    parser = create_parser()
    my_args = parser.parse_args(args)
    if not my_args:
        parser.print_usage()
        sys.exit(1)

    print('my_args: {my_args}'.format(my_args=my_args))

#  *** next 3 lines are from dotm_search ***
    path_to_search = my_args.dir
    get_special_paths(dir)

    # text_to_find = my_args.text
    # find_dotm(path_to_search, text_to_find)

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main(sys.argv[1:])
