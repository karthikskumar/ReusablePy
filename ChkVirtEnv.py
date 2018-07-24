# Script checks if python is running inside virtual environment.
import sys

if(hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)):
    virtEnv = 'Running in virtual environment.'
else:
    virtEnv = 'Not running in virtual environment.'

print(virtEnv)