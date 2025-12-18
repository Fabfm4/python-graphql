from graph_app.app.use_cases.group_use_cases import ConsultByNameGroupUseCase, ConsultAllGroupUseCase, CreateGroupUseCase
from graph_app.app.use_cases.player_use_cases import ConsultByNamePlayerUseCase, ConsultAllPlayerUseCase, CreatePlayerUseCase
from graph_app.app.use_cases.team_use_cases import ConsultByNameTeamUseCase, ConsultAllTeamUseCase, CreateTeamUseCase
from graph_app.app.use_cases.match_use_cases import CreateMatchUseCase, ConsultByNumberMatchUseCase, ConsultAllMatchUseCase
from graph_app.infrastructure.repositories.cache.cache_group_repository import CacheGroupRepository
from graph_app.infrastructure.repositories.cache.cache_player_repository import CachePlayerRepository
from graph_app.infrastructure.repositories.cache.cache_team_repository import CacheTeamRepository
from graph_app.infrastructure.repositories.cache.cache_match_repository import CacheMatchRepository
from graph_app.infrastructure.db import load_db
from graph_app.domain.entities.team_entity import Team
from graph_app.domain.entities.match_entity import GameMatch
from graph_app.domain.entities.player_entity import Player
from graph_app.domain.entities.group_entity import Group


ACTIONS = {
    'create': {
        'teams': CreateTeamUseCase,
        'matchs': CreateMatchUseCase,
        'players': CreatePlayerUseCase,
        'groups': CreateGroupUseCase,
    },
    'consult': {
        'teams': ConsultByNameTeamUseCase,
        'matchs': ConsultByNumberMatchUseCase,
        'players': ConsultByNamePlayerUseCase,
        'groups': ConsultByNameGroupUseCase,
    },
    'all': {
        'teams': ConsultAllTeamUseCase,
        'matchs': ConsultAllMatchUseCase,
        'players': ConsultAllPlayerUseCase,
        'groups': ConsultAllGroupUseCase,
    }
}

REPOSITORIES = {
    'teams': CacheTeamRepository,
    'matchs': CacheMatchRepository,
    'players': CachePlayerRepository,
    'groups': CacheGroupRepository,
}

MODELS = {
    'teams': Team,
    'matchs': GameMatch,
    'players': Player,
    'groups': Group,
}

if __name__ == '__main__':
    while True:
        db = load_db()
        model_to_work = input(f"""Enter the model to work: ({', '.join(db.keys())}: or exit): """) or "teams"
        if model_to_work == 'exit':
            exit()
        if model_to_work not in db.keys():
            print("Model not found")
            continue
    
        action = input(f"""Enter the action to perform ({', '.join(ACTIONS.keys())}): """) or "all"
        if action not in ACTIONS.keys():
            print("Action not found")
            continue

        RepositoryClass = REPOSITORIES[model_to_work]
        UseCaseClass = ACTIONS[action][model_to_work]
        use_case = UseCaseClass(RepositoryClass())
        number_of_params = use_case.execute.__code__.co_argcount
        params = use_case.execute.__code__.co_varnames
        params_to_set = params[1:number_of_params]
        fields_main_model = MODELS[model_to_work].model_fields
        result = use_case.execute()
        print(result)

    print("entra")