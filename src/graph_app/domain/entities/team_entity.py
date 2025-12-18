from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Team:
    id: int | None = None
    name: str
    flag : str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None
