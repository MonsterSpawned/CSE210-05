import os
from os import sep, linesep

import __main__

class FSUtils():
    
    def get_cwd(self):
        return os.getcwd()
    
    def get_os_path_sep(self):
        return sep
    
    def get_os_linesep(self):
        return linesep