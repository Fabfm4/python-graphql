

from typing import Optional
from graph_app.domain.entities.match_entity import GameMatch
from graph_app.domain.repositories.match_repository import MatchRepository
from graph_app.infrastructure.db import connection_db


@connection_db
class CacheMatchRepository(MatchRepository):

    def get_match_by_number(self, match_number: int) -> Optional[GameMatch]:
        record = self.filter_by_field('match_number', match_number)
        if record:
            return GameMatch(**record)

        return None

    def save(self, model: GameMatch) -> GameMatch:
        if not model.id:
            model.id = self.get_max_id() + 1
            self.add_record(model.model_dump())

        self.update_db()
