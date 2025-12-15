

from typing import Optional
from graph_app.domain.entities.team_entity import Team
from graph_app.domain.repositories.team_repository import TeamRepository
from graph_app.infrastructure.db import connection_db


@connection_db
class CacheTeamRepository(TeamRepository):

    def get_team_by_name(self, name) -> Optional[Team]:
        record = self.filter_by_field('name', name)
        if record:
            return Team(**record)

        return None

    def save(self, model: Team) -> Team:
        if not model.id:
            model.id = self.get_max_id() + 1
            self.add_record(model.model_dump())

        self.update_db()
