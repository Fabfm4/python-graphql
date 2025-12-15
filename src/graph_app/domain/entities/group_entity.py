from typing import Optional
from pydantic import BaseModel

from graph_app.domain.entities.team_entity import Team


class Group(BaseModel):
    id: Optional[int] = None
    name: str
    teams: list[tuple[int, Team]]
