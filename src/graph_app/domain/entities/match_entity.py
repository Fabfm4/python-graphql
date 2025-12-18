from graph_app.domain.entities.group_entity import Group
from graph_app.domain.entities.team_entity import Team
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class GameMatch:
    id: int | None = None
    match_number: int
    local_team: Team
    away_team: Team
    group: Group
    stadium: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None
