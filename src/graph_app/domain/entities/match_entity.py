from typing import Optional
from pydantic import BaseModel

from graph_app.domain.entities.group_entity import Group
from graph_app.domain.entities.team_entity import Team


class GameMatch(BaseModel):
    id: Optional[int] = None
    match_number: int
    local_team: Team
    away_team: Team
    group: Group
    stadium: str
