#!/usr/bin/env python2
# SPDX-License-Identifier: MIT

import os
import sys
import pdb
import glob

from operator import itemgetter

# when break, call pdb
def install_pdb():
    def info(type, value, tb):
        if hasattr(sys, 'ps1') or not sys.stderr.isatty():
            # You are in interactive mode or don't have a tty-like
            # device, so call the default hook
            sys.__execthook__(type, value, tb)
        else:
            import traceback, pdb
            # You are not in interactive mode; print the exception
            traceback.print_exception(type, value, tb)
            print
            # ... then star the debugger in post-mortem mode
            pdb.pm()

    sys.excepthook = info

# get the latest file from pn
def get_latest_file(pn):
    rtn = []
    for f in glob.glob(pn):
        rtn.append([f, os.stat(f).st_mtime])
    if len(rtn) == 0:
        return None
    return max(rtn, key=itemgetter(1))[0]

# iter down to zero
def to_zero(start):
    return range(start-1, -1, -1)

# clean split
def split(line, tok):
    (lhs, rhs) = line.rsplit(tok, 1)
    return (lhs.strip(), rhs.strip())

# get content
def read_file(pn):
    data = ""
    with open(pn) as fd:
        data = fd.read()
    return data
