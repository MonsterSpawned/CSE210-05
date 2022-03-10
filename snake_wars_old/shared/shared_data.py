from log21 import Levels

from snake_wars.utils.fs_utils import FSUtils
from snake_wars.utils.log_utils import LogUtils
from snake_wars.utils.cfg_utils import ConfigUtils

# Do score managing and other miscellaneous shared functions in here...
class SharedData():
    
    def __init__(self, debug: bool = False):
        self.config_utils = ConfigUtils()
        self.fs_utils = FSUtils()
        self.log_utils = LogUtils(self.game_name, self.log_level)
        self._debug = debug
        
        self.game_name = self.config_utils.get_cfg_string("game_name")
        self.game_name = self.config_utils.get_cfg_int("window_width")
        self.game_name = self.config_utils.get_cfg_int("window_height")
        self.game_fps = self.config_utils.get_cfg_string("game_fps")
        self.root_dir = self.fs_utils.get_cwd()
        self.path_sep = self.fs_utils.get_os_path_sep()
        self.line_sep = self.fs_utils.get_os_linesep()      
        
        self.COLUMNS = 40
        self.ROWS = 20
        self.CELL_SIZE = 15
        self.MAX_X = 900
        self.MAX_Y = 600
        
    def get_log_level(self):
        if self.config_utils.get_cfg_string("log_level") in ["DEBUG", "DBG"]: 
            self.log_level = Levels.DEBUG
        elif self.config_utils.get_cfg_string("log_level") in ["INFORMATION", "INFO"]: 
            self.log_level = Levels.INFO
        elif self.config_utils.get_cfg_string("log_level") in ["WARNING", "WARN"]: 
            self.log_level = Levels.WARN
        elif self.config_utils.get_cfg_string("log_level") in ["ERROR", "ERR"]: 
            self.log_level = Levels.ERROR
        elif self.config_utils.get_cfg_string("log_level") in ["CRITICAL", "FATAL", "CRIT"]: 
            self.log_level = Levels.CRITICAL
        else:
            self.log_level = Levels.INFO