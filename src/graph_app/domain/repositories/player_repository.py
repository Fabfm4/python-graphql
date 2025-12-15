

from abc import ABC, abstractmethod
from typing import Optional

from graph_app.domain.entities.player_entity import Player
from graph_app.domain.repositories._common import CrudRepository


class PlayerRepository(ABC, CrudRepository[Player]):

    def __init__(self) -> None:
        super().__init__()
        self.table = "players"

    @abstractmethod
    def get_player_by_name(self, name) -> Optional[Player]:
        raise NotImplementedError

    @abstractmethod
    def save(self, model: Player) -> Player:
        raise NotImplementedError
