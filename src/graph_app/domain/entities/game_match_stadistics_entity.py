from enum import Enum
from graph_app.domain.entities.match_entity import GameMatch
from graph_app.domain.entities.player_entity import Player
from graph_app.domain.entities.team_entity import Team
from dataclasses import dataclass, field
from datetime import datetime


class EventGameMatch(str, Enum):
    GOAL = 'GOAL'
    YELLOW_CARD = 'YELLOW_CARD'
    RED_CARD = 'RED_CARD'


@dataclass
class GameMatchStadistics:
    id: int | None = None
    game_match: GameMatch
    event: EventGameMatch
    team: Team
    player: Player
    minute: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None
