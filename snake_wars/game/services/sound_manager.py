# An optional class. We may or may not use it. Would be a "fun addition," if we have the time.
import distro # To be used in future games... :)
from platform import system, release, version

class SoundManager():
    # Play sounds, imports sounds, etc. on multiple OSes.

    def __init__(self):
        print(f"Current OS: {system} {release} (v{version})")
    
    def play_sound(self, path: str):
        if system() == "Windows":
            import winsound
            winsound.PlaySound(path, winsound.SND_ASYNC)
        elif system() == "Linux":
            pass # TODO: #1 Do linux related sound things here...