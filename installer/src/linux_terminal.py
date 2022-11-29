#!/bin/bash
import os

from .terminal import Terminal

class LinuxTerminal(Terminal):
    def touch_file(self, the_file : str):
        exit_code = os.system(f"touch {the_file}")
        if exit_code != 0:
            raise ValueError(f"cannot touch file {the_file}")

    def copy_file(self, the_file : str, the_destination : str):
        exit_code = os.system(f"cp {the_file} {the_destination}")
        if exit_code != 0:
            raise ValueError(f"cannot copy file {the_file} to {the_destination}")
    
    def move_file(self, the_file : str, the_destination : str):
        exit_code = os.system(f"mv {the_file} {the_destination}")
        if exit_code != 0:
            raise ValueError(f"cannot move file {the_file} to {the_destination}")
    
    def delete_file(self, the_file : str):
        exit_code = os.system(f"rm {the_file}")
        if exit_code != 0:
            raise ValueError(f"cannot delete file {the_file}")

    def create_directory(self, the_directory : str):
        exit_code = os.system(f"mkdir -p {the_directory}")
        if exit_code != 0:
            raise ValueError(f"cannot create directory {the_directory}")
        
    def delete_directory(self, the_directory : str):
        exit_code = os.system(f"rm -rf {the_directory}")
        if exit_code != 0:
            raise ValueError(f"cannot delete directory {the_directory}")
