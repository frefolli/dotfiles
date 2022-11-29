from .repository import Repository
from .repository_factory import RepositoryFactory

class Context:
    _repository = None

    @staticmethod
    def set_repository(repository : Repository):
        Context._repository = repository

    @staticmethod
    def get_repository():
        if Context._repository == None:
            Context.set_repository(RepositoryFactory.from_location("./repository"))
        return Context._repository
