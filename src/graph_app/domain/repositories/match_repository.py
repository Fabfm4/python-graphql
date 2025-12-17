

from abc import ABC, abstractmethod
from typing import Optional

from graph_app.domain.entities.match_entity import GameMatch
from graph_app.domain.repositories._common import CrudRepository


class MatchRepository(ABC, CrudRepository[GameMatch]):

    def __init__(self) -> None:
        super().__init__()
        self.table = "matchs"

    @abstractmethod
    def get_match_by_number(self, match_number: int) -> Optional[GameMatch]:
        raise NotImplementedError

    @abstractmethod
    def save(self, model: GameMatch) -> GameMatch:
        raise NotImplementedError
