"""
class Package
"""
from .serializable import Serializable
from .metadata import Metadata
from .files import Files
from .commands import Commands
from .dependencies import Dependencies

class Package(Serializable):
    def __init__(self, metadata : Metadata, dependencies : Dependencies,
                 content : Files, post_install : Commands):
        self._metadata = metadata
        self._dependencies = dependencies
        self._content = content
        self._post_install = post_install

    def get_metadata(self):
        return self._metadata
    
    def get_content(self):
        return self._content

    def get_post_install(self):
        return self._post_install

    def get_dependencies(self):
        return self._dependencies

    def to_str(self):
        return (
            "Package(" +
                "metadata = " + self.get_metadata().to_str() + ", " +
                "dependencies = " + self.get_dependencies().to_str() + ", " +
                "content = " + self.get_content().to_str() + ", " +
                "post_install = " + self.get_post_install().to_str() +
            ")"
        )

    def to_dict(self):
        return {
            "metadata": self.get_metadata().to_dict(),
            "dependencies": self.get_dependencies().to_dict(),
            "content": self.get_content().to_dict(),
            "post_install": self.get_post_install().to_dict()
        }

    def install(self, location : str):
        print(f"[ WORKING ] {self._metadata.get_name()}")
        self._dependencies.install()
        self._content.install(location)
        self._post_install.run()
        print(f"[  DONE   ] {self._metadata.get_name()}")
