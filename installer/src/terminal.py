"""
class Terminal
"""
from .template_method_exception import TemplateMethodException

class Terminal:
    def touch_file(self, the_file : str):
        raise TemplateMethodException()

    def copy_file(self, the_file : str, the_destination : str):
        raise TemplateMethodException()

    def move_file(self, the_file : str, the_destination : str):
        raise TemplateMethodException()

    def delete_file(self, the_file : str):
        raise TemplateMethodException()

    def create_directory(self, the_directory : str):
        raise TemplateMethodException()
    
    def delete_directory(self, the_directory : str):
        raise TemplateMethodException()
