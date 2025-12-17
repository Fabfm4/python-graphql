from tokenize import group
from graph_app.app.use_cases.group_use_cases import ConsultGroupUseCase, CreateGroupUseCase
from graph_app.app.use_cases.player_use_cases import ConsultPlayerUseCase, CreatePlayerUseCase
from graph_app.app.use_cases.team_use_cases import ConsultTeamUseCase, CreateTeamUseCase
from graph_app.app.use_cases.match_use_cases import CreateMatchUseCase, ConsultMatchUseCase
from graph_app.infrastructure.repositories.cache.cache_group_repository import CacheGroupRepository
from graph_app.infrastructure.repositories.cache.cache_player_repository import CachePlayerRepository
from graph_app.infrastructure.repositories.cache.cache_team_repository import CacheTeamRepository
from graph_app.infrastructure.repositories.cache.cache_match_repository import CacheMatchRepository

if __name__ == '__main__':
    cache_team_repository = CacheTeamRepository()
    consult_team_use_case = ConsultTeamUseCase(cache_team_repository)

    cache_group_repository = CacheGroupRepository()
    create_group_use_case = CreateGroupUseCase(cache_group_repository)
    consult_group_use_case = ConsultGroupUseCase(cache_group_repository)

    cache_player_repository = CachePlayerRepository()
    create_player_use_case = CreatePlayerUseCase(cache_player_repository)
    consult_player_use_case = ConsultPlayerUseCase(cache_player_repository) 

    cache_match_repository = CacheMatchRepository()
    create_match_use_case = CreateMatchUseCase(cache_match_repository)
    consult_match_use_case = ConsultMatchUseCase(cache_match_repository)
    
    mexico = consult_team_use_case.execute('Mexico')
    south_africa = consult_team_use_case.execute('South Africa')
    korea = consult_team_use_case.execute('Korea')
    irland = consult_team_use_case.execute('Irland')

    print(mexico)
    print(south_africa)
    print(korea)
    print(irland)
    teams = [(1, mexico), (2, south_africa), (3, korea), (4, irland)]

    group_a = consult_group_use_case.execute('A')
    print(group_a)


    player = consult_player_use_case.execute("Rafael Marquez")
    print(player)

    match_2 = create_match_use_case.execute(2, korea, irland, group_a, "Stadium")
    print(match_2)
    match_3 = create_match_use_case.execute(3, mexico, korea, group_a, "Stadium")
    print(match_3)
    match_4 = create_match_use_case.execute(4, irland, south_africa, group_a, "Stadium")
    print(match_4)
    
    match_5 = create_match_use_case.execute(5, irland, mexico, group_a, "Stadium")
    print(match_5)
    match_6 = create_match_use_case.execute(6, south_africa, korea, group_a, "Stadium")
    print(match_6)







    print("entra")