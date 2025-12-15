from typing import Optional
from pydantic import BaseModel

from graph_app.domain.entities.team_entity import Team


class Player(BaseModel):
    id: Optional[int] = None
    name: str
    photo: str
    team: Team
    number: int
