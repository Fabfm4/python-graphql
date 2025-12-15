from typing import Optional
from pydantic import BaseModel

from graph_app.domain.entities.group_entity import Group
from graph_app.domain.entities.team_entity import Team


class TeamStadistics(BaseModel):
    id: Optional[int] = None
    team: Team
    group: Group
    points: Optional[int] = 0
    match_win: Optional[int] = 0
    match_tie: Optional[int] = 0
    march_lose: Optional[int] = 0
