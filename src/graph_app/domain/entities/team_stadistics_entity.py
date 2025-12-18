from graph_app.domain.entities.group_entity import Group
from graph_app.domain.entities.team_entity import Team
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class TeamStadistics:
    id: int | None = None
    team: Team
    group: Group
    points: int | None = 0
    match_win: int | None = 0
    match_tie: int | None = 0
    march_lose: int | None = 0
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None
