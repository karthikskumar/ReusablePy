"""
intellImport

Usage:          intellmport('packageName')
Description:    'intellImport' function imports a package if
                already installed, else it will first be
                installed and imported.
"""

__author__ = 'krthkskmr'
__version__ = '0.1'
__date__ = '2018-07-27'

try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain

def intellImport(package):
    if hasattr(package, "__len__") and (not isinstance(package, str)):
        package = list(package)
        for each in package:
            try:
                __import__(each)
            except ImportError:
                pipmain(['install', each])
                __import__(each)
    else:
        try:
            __import__(package)
        except ImportError:
            pipmain(['install', package])
            __import__(package)