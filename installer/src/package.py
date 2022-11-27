from .serializable import Serializable
from .metadata import Metadata
from .files import Files
from .commands import Commands

class Package(Serializable):
    def __init__(self, metadata : Metadata,
                 content : Files, post_install : Commands):
        self._metadata = metadata
        self._content = content
        self._post_install = post_install

    def get_metadata(self):
        return self._metadata
    
    def get_content(self):
        return self._content

    def get_post_install(self):
        return self._post_install

    def to_str(self):
        return (
            "Package(" +
                "metadata = " + self.get_metadata().to_str() + ", " +
                "content = " + self.get_content().to_str() + ", " +
                "post_install = " + self.get_post_install().to_str() +
            ")"
        )

    def to_dict(self):
        return {
            "type": "package",
            "metadata": self.get_metadata().to_dict(),
            "content": self.get_content().to_dict(),
            "post_install": self.get_post_install().to_dict()
        }
