from random import shuffle


teams_no = 12
games_no = 6
rounds_no = 6


class NotPossible(Exception):
    pass


def get_schema():

    teams_data = {
        team_no: {
            'rounds': [],
            'games': [],
            'opponents': []
        }
        for team_no in range(teams_no)
    }

    schema = {}

    for round_no in range(0, rounds_no):

        schema[round_no] = {}

        for game_no in range(games_no):

            def get_team(exclude_teams=[]):

                teams_list = range(0, teams_no)
                shuffle(teams_list)

                for team_no in teams_list:

                    if (
                        team_no in exclude_teams
                        or round_no in teams_data[team_no]['rounds']
                        or game_no in teams_data[team_no]['games']
                    ):
                        continue

                    return team_no

                raise NotPossible()

            def add_team_data(team_no, round_no, game_no, opponent_no):
                teams_data[team_no]['rounds'].append(round_no)
                teams_data[team_no]['games'].append(game_no)
                teams_data[team_no]['opponents'].append(opponent_no)

            team1 = get_team()
            team2 = get_team(exclude_teams=[team1] + teams_data[team1]['opponents'])

            add_team_data(team1, round_no, game_no, team2)
            add_team_data(team2, round_no, game_no, team1)

            schema[round_no][game_no] = (team1, team2)

    return schema

successful = False

while not successful:
    try:
        schema = get_schema()
    except NotPossible:
        pass
    else:
        successful = True

for round_no, games in schema.items():

    print("\nround {}".format(round_no))

    for game_no, teams in games.items():
        print("  game {}:  {} - {}".format(game_no, teams[0], teams[1]))

print('')
