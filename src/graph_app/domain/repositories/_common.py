

from abc import abstractmethod
from typing import Generic, TypeVar

from pydantic import BaseModel



T = TypeVar("T", bound=BaseModel)


class CrudRepository(Generic[T]):
    @abstractmethod
    def save(self, model: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id_entity: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id_entity: int) -> T:
        raise NotImplementedError
