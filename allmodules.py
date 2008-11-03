"""Use the AllModules plugin with --with-all-modules to enable collection
and execution of tests in any *.py module, not only those matching
TESTMATCH. This allows tests to be placed in any file, a la py.test"""

import os
from nose.plugins.base import Plugin

class AllModules(Plugin):
    """
    Collect tests in all *.py modules.
    """

    enabled = False
    name = "all-modules"
    
    def wantFile(self, file):
        # always want .py files
        if file.endswith('.py'):
            return True
    
    def wantModule(self, module):
        return True
