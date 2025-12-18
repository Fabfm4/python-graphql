

from abc import ABC, abstractmethod
from typing import Optional

from graph_app.domain.entities.team_entity import Team
from graph_app.domain.repositories._common import CrudRepository


class TeamRepository(ABC, CrudRepository[Team]):

    def __init__(self) -> None:
        super().__init__()
        self.table = "teams"

    @abstractmethod
    def get_team_by_name(self, name) -> Optional[Team]:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Team]:
        raise NotImplementedError

    @abstractmethod
    def save(self, model: Team) -> Team:
        raise NotImplementedError
