

from graph_app.domain.entities.team_entity import Team
from graph_app.domain.entities.group_entity import Group
from graph_app.domain.exceptions import DuplicateRecordError
from graph_app.domain.repositories.group_repository import GroupRepository
from graph_app.app.use_cases._common import CommonUseCase


type PositionGroup = tuple[position:int, team:Team]


class GroupUseCases(CommonUseCase[GroupRepository, Group]):
    def __init__(self, repo: GroupRepository):
        super().__init__(repo)

class CreateGroupUseCase(GroupUseCases):

    def execute(self, name: str, teams: list[PositionGroup], **kwargs) -> Group:
        group_search = self.repo.get_group_by_name(name=name)
        if group_search:
            raise DuplicateRecordError

        new_group = self.repo.save(Group(name=name, teams=teams))
        return new_group


class ConsultByNameGroupUseCase(GroupUseCases):

    def execute(self, name: str, *args, **kwargs) -> Group:
        group_search = self.repo.get_group_by_name(name=name)
        if group_search:
            return group_search

        return None
        

class ConsultAllGroupUseCase(GroupUseCases):
    def execute(self, *args, **kwargs) -> list[Group]:
        return self.repo.get_all()
