

from graph_app.domain.entities.team_entity import Team
from graph_app.domain.exceptions import DuplicateRecordError
from graph_app.domain.repositories.team_repository import TeamRepository
from graph_app.domain.use_cases._common import CommonUseCase


class CreateTeamUseCase(CommonUseCase[TeamRepository, Team]):

    def execute(self, name, flag, **kwargs) -> Team:
        team_search = self.repo.get_team_by_name(name=name)
        if team_search:
            raise DuplicateRecordError

        new_team = self.repo.save(Team(name=name, flag=flag))
        return new_team


class ConsultTeamUseCase(CommonUseCase[TeamRepository, Team]):

    def execute(self, name: str, *args, **kwargs) -> Team:
        team_search = self.repo.get_team_by_name(name=name)
        if team_search:
            return team_search

        return None
        