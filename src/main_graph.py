from tokenize import group
from graph_app.app.use_cases.group_use_cases import ConsultGroupUseCase, CreateGroupUseCase
from graph_app.app.use_cases.player_use_cases import CreatePlayerUseCase
from graph_app.app.use_cases.team_use_cases import ConsultTeamUseCase, CreateTeamUseCase
from graph_app.infrastructure.repositories.cache.cache_group_repository import CacheGroupRepository
from graph_app.infrastructure.repositories.cache.cache_player_repository import CachePlayerRepository
from graph_app.infrastructure.repositories.cache.cache_team_repository import CacheTeamRepository


if __name__ == '__main__':
    cache_team_repository = CacheTeamRepository()
    consult_team_use_case = ConsultTeamUseCase(cache_team_repository)

    cache_group_repository = CacheGroupRepository()
    create_group_use_case = CreateGroupUseCase(cache_group_repository)
    consult_group_use_case = ConsultGroupUseCase(cache_group_repository)

    cache_player_repository = CachePlayerRepository()
    create_player_use_case= CreatePlayerUseCase(cache_player_repository)
    
    mexico = consult_team_use_case.execute('Mexico')
    south_africa = consult_team_use_case.execute('South Africa')
    korea = consult_team_use_case.execute('Korea')
    irland = consult_team_use_case.execute('Irland')

    print(mexico)
    print(south_africa)
    print(korea)
    print(irland)
    teams = [(1, mexico), (2, south_africa), (3, korea), (4, irland)]

    # group_a = create_group_use_case.execute('A', teams)
    group_a = consult_group_use_case.execute('A')
    print(group_a)


    player = create_player_use_case.execute("Rafael Marquez", "jpg", mexico, 4)





    print("entra")