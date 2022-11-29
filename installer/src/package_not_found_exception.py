class PackageNotFoundException(Exception):
    def __init__(self, name):            
        super().__init__(f"couldn't find {name} in repository")
