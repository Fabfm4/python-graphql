

from typing import Optional
from graph_app.domain.entities.player_entity import Player
from graph_app.domain.repositories.player_repository import PlayerRepository
from graph_app.infrastructure.db import connection_db


@connection_db
class CachePlayerRepository(PlayerRepository):

    def get_player_by_name(self, name) -> Optional[Player]:
        record = self.filter_by_field('name', name)
        if record:
            return Player(**record)

        return None

    def save(self, model: Player) -> Player:
        if not model.id:
            model.id = self.get_max_id() + 1
            self.add_record(model.model_dump())

        self.update_db()
