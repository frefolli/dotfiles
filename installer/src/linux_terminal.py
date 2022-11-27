#!/bin/bash
import os

from .terminal import Terminal

class LinuxTerminal(Terminal):
    def touch_file(self, the_file : str):
        os.system(f"touch {the_file}")

    def copy_file(self, the_file : str, the_destination : str):
        os.system(f"cp {the_file} {the_destination}")

    def move_file(self, the_file : str, the_destination : str):
        os.system(f"mv {the_file} {the_destination}")

    def delete_file(self, the_file : str):
        os.system(f"rm {the_file}")
