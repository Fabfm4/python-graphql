

from graph_app.domain.entities.team_entity import Team
from graph_app.domain.exceptions import DuplicateRecordError
from graph_app.domain.repositories.team_repository import TeamRepository
from graph_app.app.use_cases._common import CommonUseCase


class TeamUseCases(CommonUseCase[TeamRepository, Team]):
    def __init__(self, repo: TeamRepository):
        super().__init__(repo)


class CreateTeamUseCase(TeamUseCases):

    def execute(self, name, flag, **kwargs) -> Team:
        team_search = self.repo.get_team_by_name(name=name)
        if team_search:
            raise DuplicateRecordError

        new_team = self.repo.save(Team(name=name, flag=flag))
        return new_team


class ConsultByNameTeamUseCase(TeamUseCases):

    def execute(self, name: str, *args, **kwargs) -> Team:
        team_search = self.repo.get_team_by_name(name=name)
        if team_search:
            return team_search

        return None
        

class ConsultAllTeamUseCase(TeamUseCases):
    def execute(self, *args, **kwargs) -> list[Team]:
        return self.repo.get_all()
