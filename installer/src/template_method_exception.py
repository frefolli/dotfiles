class TemplateMethodException(Exception):
    def __init__(self):            
        super().__init__("unable to simply call a template method")
