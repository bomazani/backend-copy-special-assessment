#!/usr/bin/env python

"""Copy Special exercise
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

__author__ = 'bomazani, madarp'

import sys
import re
import os
import shutil
import commands
import argparse
import zipfile



def get_special_paths(dir):
    paths = []
    ### returns a list of the absolute paths of the special files in the given directory ###
    # need to change to >>> os.listdir(dir):
    for file in os.listdir(dir):  
        if re.search(r'\__\w*\__', file):
            paths.append(os.path.abspath(os.path.join(dir, file)))
    return paths


def copy_to(paths, todir):
    ## given a list of absolue paths, copy the files into the given directory ##
    if not os.path.isdir(todir):
        os.makedirs(todir)
    todir_path = os.path.abspath(todir)
    for path in paths:
        shutil.copy(path, todir_path)


def zip_to(paths, zippath):
    ### given a list of absolute paths, zip those files up into the given destination file ###
    zip_it = 'zip -j {} '.format(zippath)
    zip_it += ' '.join(paths)
    print("Command I'm going to do: \n {}".format(zip_it))
    status, output = commands.getstatusoutput(zip_it)
    if status:
        print(output)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--dir', help='source directory of files to search', default='.')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    return parser


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

    my_paths = get_special_paths(path_to_search)

    if dest_path:
        copy_to(my_paths, dest_path)
    elif zip_path:
        zip_to(my_paths, zip_path)
    else:
        print('Here are the special files: {}'.format("\n".join(my_paths)))


if __name__ == "__main__":
    # the following line shaves the program file name off of the command line args
    my_args = sys.argv[1:]
    # print my_args
    main(my_args)