from .linux_terminal import LinuxTerminal
import os

class TerminalFactory:
    @staticmethod
    def get_terminal():
        the_os_name = os.name
        if the_os_name == "posix":
            return LinuxTerminal()
        else:
            raise ValueError("OS not supported")
