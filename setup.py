#!/usr/bin/env python

"""
setup.py file for pygroupcidr
"""

from distutils.core import setup, Extension


groupcidr_module = Extension('_groupcidr',
                           include_dirs = ['/usr/include/python3.7m'],
                           sources=['groupcidr_wrap.c', 'groupcidr.c'],
                           )

setup (name = 'groupcidr',
       version = '0.1',
       author      = "Ayushman Dutta",
       description = """groupcidr wrapper for python""",
       ext_modules = [groupcidr_module],
       py_modules = ["groupcidr"],
       )
