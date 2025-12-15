from enum import Enum
from typing import Optional

from pydantic import BaseModel

from graph_app.domain.entities.match_entity import GameMatch
from graph_app.domain.entities.player_entity import Player
from graph_app.domain.entities.team_entity import Team


class EventGameMatch(str, Enum):
    GOAL = 'GOAL'
    YELLOW_CARD = 'YELLOW_CARD'
    RED_CARD = 'RED_CARD'


class GameMatchStadistics(BaseModel):
    id: Optional[int] = None
    game_match: GameMatch
    event: EventGameMatch
    team: Team
    player: Player
    minute: int
