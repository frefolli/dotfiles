#!/bin/bash

class Terminal:
    def touch_file(self, the_file : str):
        raise Exception("template method")

    def copy_file(self, the_file : str, the_destination : str):
        raise Exception("template method")

    def move_file(self, the_file : str, the_destination : str):
        raise Exception("template method")

    def delete_file(self, the_file : str):
        raise Exception("template method")

    def create_directory(self, the_directory : str):
        raise Exception("template method")
    
    def delete_directory(self, the_directory : str):
        raise Exception("template method")
