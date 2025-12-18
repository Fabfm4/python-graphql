

from graph_app.domain.entities.player_entity import Player
from graph_app.domain.entities.team_entity import Team
from graph_app.domain.exceptions import DuplicateRecordError
from graph_app.domain.repositories.player_repository import PlayerRepository
from graph_app.app.use_cases._common import CommonUseCase


class PlayerUseCases(CommonUseCase[PlayerRepository, Player]):
    def __init__(self, repo: PlayerRepository):
        super().__init__(repo)


class CreatePlayerUseCase(PlayerUseCases):

    def execute(self, name: str, photo: str, team: Team, number: int,  **kwargs) -> Player:
        player_search = self.repo.get_player_by_name(name=name)
        if player_search:
            raise DuplicateRecordError

        new_player = self.repo.save(Player(
            name=name,
            photo=photo,
            team=team,
            number=number
            
        ))
        return new_player


class ConsultByNamePlayerUseCase(PlayerUseCases):

    def execute(self, name: str, *args, **kwargs) -> Player:
        player_search = self.repo.get_player_by_name(name=name)
        if player_search:
            return player_search

        return None


class ConsultAllPlayerUseCase(PlayerUseCases):
    def execute(self, *args, **kwargs) -> list[Player]:
        return self.repo.get_all()
