from graph_app.domain.entities._common import Catalog, TimeStamp
from graph_app.domain.entities.team_entity import Team
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Group:
    id: int | None = None
    name: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None


@dataclass
class GroupInitialPosition:
    group: Group
    team: Team
    position: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None
