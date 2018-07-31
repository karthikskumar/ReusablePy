"""
chkEnv()

Usage:          chkEnv()
Description:    Script checks if python is running inside virtual environment.
"""

__author__ = 'krthkskmr'
__version__ = '0.1'
__date__ = '2018-07-27'

import sys

def chkEnv():
    if(hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)):
        virtEnv = 'Running in virtual environment.'
    else:
        virtEnv = 'Not running in virtual environment.'

    print(virtEnv)