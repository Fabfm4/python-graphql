from graph_app.domain.entities.team_entity import Team
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Player:
    id: int | None = None
    name: str
    photo : str
    team: Team
    number: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None
