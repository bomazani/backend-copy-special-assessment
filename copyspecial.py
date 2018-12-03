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
import zipfile

"""Copy Special exercise
"""


def get_special_paths(dir):
    paths = []
    ### returns a list of the absolute paths of the special files in the given directory ###
    # need to change to >>> os.listdir(dir):
    for __, __, files in os.walk(dir):  
        for filename in files:
            if re.search(r'\__\w*\__', filename):
                paths.append(os.path.abspath(filename))
    return paths


def copy_to(paths, todir):
    if not os.path.isdir(todir):
        os.makedirs(todir)
    todir_path = os.path.abspath(todir)
    for path in paths:
        shutil.copy(path, todir_path)
#     return is not needed


def zip_to(paths, zippath):
    ### given a list of paths, zip those files up into the given zipfile ###
    ### command line: $ python copyspecial.py --tozip 'new zip file name' -d 'folder/files to compress'
    print("I'm zippy!")
    # contents = commands.getstatusoutput("ls " + str(zippath))
    # subcontents = contents[1].split('\n')
    # print(subcontents)
    # zip_it = 'zip -j zippath ' + str(contents[1].split('\n'))
    # print(zip_it)
    # commands.getstatusoutput(zip_it)
    for file in paths:
        zip_it = 'zip -j {} {}'.format(zippath, file)
        commands.getstatusoutput(zip_it)
        print(zip_it)


    # commands.getstatusoutput('zip -j zippath ' + str(subcontents))
    # commands.getstatusoutput('zip -j zippath ' + str(contents[1].split('\n')))


def create_parser():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--dir', help='source directory of files to search', default='.')
    # parser.add_argument(
    #     'dir', help='source directory of files to search', default='.')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'

    return parser

# Write functions and modify main() to call them


def main(args):
    parser = create_parser()
    my_args = parser.parse_args(args)
    if not my_args:
        parser.print_usage()
        sys.exit(1)

    print('my_args: {my_args}'.format(my_args=my_args))

    path_to_search = my_args.dir
    dest_path = my_args.todir
    zip_path = my_args.tozip

    # assign variable to the output of the first function 
    my_paths = get_special_paths(path_to_search)

    # Business logic: 
    # Choose one of three ways to process the my_paths list,
    # based on cmd line options present or not present
    if dest_path:
        copy_to(my_paths, dest_path)
    elif zip_path:
        zip_to(my_paths, zip_path)
    else:
        print('Here are the special files: {}'.format("\n".join(my_paths)))



    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # Call your functions


if __name__ == "__main__":
    # the following line shaves the program file name off of the command line args
    my_args = sys.argv[1:]
    # print my_args
    main(my_args)