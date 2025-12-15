
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pydantic import BaseModel


Repository = TypeVar("Repository")
T = TypeVar("T", bound=BaseModel)


class CommonUseCase(ABC, Generic[Repository, T]):

    def __init__(self, repo: Repository):
        self.repo: Repository = repo

    @abstractmethod
    def execute(self, *args, **kwargs) -> T:
        raise NotImplementedError
