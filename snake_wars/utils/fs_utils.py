import os
from os import sep, linesep

from snake_wars.__main__ import Game

class FSUtils():
    
    def get_cwd(self):
        return os.path.abspath(Game)
    
    def get_os_path_sep(self):
        return sep
    
    def get_os_linesep(self):
        return linesep