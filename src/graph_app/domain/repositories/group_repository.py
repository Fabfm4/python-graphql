

from abc import ABC, abstractmethod
from typing import Optional

from graph_app.domain.entities.group_entity import Group
from graph_app.domain.repositories._common import CrudRepository


class GroupRepository(ABC, CrudRepository[Group]):

    def __init__(self) -> None:
        super().__init__()
        self.table = "groups"

    @abstractmethod
    def get_group_by_name(self, name) -> Optional[Group]:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Group]:
        raise NotImplementedError

    @abstractmethod
    def save(self, model: Group) -> Group:
        raise NotImplementedError
