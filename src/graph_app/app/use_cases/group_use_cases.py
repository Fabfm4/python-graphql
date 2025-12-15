

from graph_app.domain.entities.group_entity import Group
from graph_app.domain.exceptions import DuplicateRecordError
from graph_app.domain.repositories.group_repository import GroupRepository
from graph_app.app.use_cases._common import CommonUseCase


class CreateGroupUseCase(CommonUseCase[GroupRepository, Group]):

    def execute(self, name: str, teams: list[tuple[Group]], **kwargs) -> Group:
        group_search = self.repo.get_group_by_name(name=name)
        if group_search:
            raise DuplicateRecordError

        new_group = self.repo.save(Group(name=name, teams=teams))
        return new_group


class ConsultGroupUseCase(CommonUseCase[GroupRepository, Group]):

    def execute(self, name: str, *args, **kwargs) -> Group:
        group_search = self.repo.get_group_by_name(name=name)
        if group_search:
            return group_search

        return None
        