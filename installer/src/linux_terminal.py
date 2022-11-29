#!/bin/bash
import os

from .terminal import Terminal

class LinuxTerminal(Terminal):
    def touch_file(self, the_file : str):
        exit_code = os.system(f"touch {the_file}")

    def copy_file(self, the_file : str, the_destination : str):
        exit_code = os.system(f"cp {the_file} {the_destination}")

    def move_file(self, the_file : str, the_destination : str):
        exit_code = os.system(f"mv {the_file} {the_destination}")

    def delete_file(self, the_file : str):
        exit_code = os.system(f"rm {the_file}")

    def create_directory(self, the_directory : str):
        exit_code = os.system(f"mkdir -p {the_directory}")
    
    def delete_directory(self, the_directory : str):
        exit_code = os.system(f"rm -rf {the_directory}")
