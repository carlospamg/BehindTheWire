"""
This is a very simple module to import the parent directory to the system path
so that all the test files are able to correctly import the required module
under test
"""
import os
import sys

# Import the parent directory into the system path
sys.path.append( os.path.join(os.path.dirname(__file__), '..') )
