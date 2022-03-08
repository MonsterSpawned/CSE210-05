from configparser import ConfigParser
import os
import snake_wars.__main__

from snake_wars.utils.fs_utils import FSUtils

class ConfigUtils():
    def __init__(self):
        cwd = os.path.abspath(snake_wars.__main__)
        sep = self.fs_utils.get_os_path_sep()
        cfg_dir = f"{cwd}{sep}_config{sep}"
        cfg_filename = "config.ini"
        if os.path.exists(cfg_dir) == False:
            try: 
                os.mkdir(cfg_dir) 
            except OSError as error: 
                print(error)  
        self.fs_utils = FSUtils()
        self.configuration = ConfigParser()
        self.configuration.read(cfg_dir + cfg_filename, encoding="utf-8")
        if not self.configuration.has_section("GAME"):
            self.configuration.add_section("GAME")
            self.configuration.set("GAME", "game_name", "Snake Game")
            self.configuration.set("GAME", "window_width", 1080)
            self.configuration.set("GAME", "window_height", 720)
            self.configuration.set("GAME", "game_fps", 60)
        
    def get_cfg(self):
        return self.configuration
        
    def get_cfg_bool(self, value_var):
        return self.get_cfg().getboolean("GAME", value_var, fallback=None)
    
    def get_cfg_string(self, value_var):
        return self.get_cfg().get("GAME", vars=value_var, fallback=None)
    
    def get_cfg_int(self, value_var):
        return self.get_cfg().getint("GAME", value_var, fallback=None)
    
    def get_cfg_float(self, value_var):
        return self.get_cfg().getfloat("GAME", value_var, fallback=None)