

from typing import Optional
from graph_app.domain.entities.group_entity import Group
from graph_app.domain.repositories.group_repository import GroupRepository
from graph_app.infrastructure.db import connection_db


@connection_db
class CacheGroupRepository(GroupRepository):

    def get_group_by_name(self, name) -> Optional[Group]:
        record = self.filter_by_field('name', name)
        if record:
            return Group(**record)

        return None
    
    def get_all(self) -> list[Group]:
        return [Group(**record) for record in self.get_all_records()]

    def save(self, model: Group) -> Group:
        if not model.id:
            model.id = self.get_max_id() + 1
            self.add_record(model.model_dump())
            return model

        self.update_db()
