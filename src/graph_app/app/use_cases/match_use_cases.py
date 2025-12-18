

from graph_app.domain.entities.match_entity import GameMatch
from graph_app.domain.entities.group_entity import Group
from graph_app.domain.entities.team_entity import Team
from graph_app.domain.exceptions import DuplicateRecordError
from graph_app.domain.repositories.match_repository import MatchRepository
from graph_app.app.use_cases._common import CommonUseCase


class MatchUseCase(CommonUseCase[MatchRepository, GameMatch]):
    def __init__(self, repo: MatchRepository):
        super().__init__(repo)


class CreateMatchUseCase(MatchUseCase):

    def execute(self, match_number: int, local_team: Team, away_team: Team, group: Group, stadium: str, **kwargs) -> GameMatch:
        match_search = self.repo.get_match_by_number(match_number=match_number)
        if match_search:
            raise DuplicateRecordError

        new_match = self.repo.save(GameMatch(match_number=match_number, local_team=local_team, away_team=away_team, group=group, stadium=stadium))
        return new_match


class ConsultByNumberMatchUseCase(MatchUseCase):

    def execute(self, match_number: int, *args, **kwargs) -> GameMatch:
        match_search = self.repo.get_match_by_number(number=match_number)
        if match_search:
            return match_search

        return None


class ConsultAllMatchUseCase(MatchUseCase):

    def execute(self, *args, **kwargs) -> list[GameMatch]:
        return self.repo.get_all()
