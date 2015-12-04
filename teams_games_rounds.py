teams_no = 6
games_no = 3
rounds_no = 3

teams_data = {
    team_no: {
        'rounds': [],
        'games': [],
        'opponents': []
    }
    for team_no in range(teams_no)
}

for round_no in range(rounds_no):

    print("\nround {}\n".format(round_no))

    for game_no in range(games_no):

        def get_team(exclude_teams=[]):

            for team_no in range(teams_no):

                if (
                    team_no in exclude_teams
                    or round_no in teams_data[team_no]['rounds']
                    or game_no in teams_data[team_no]['games']
                ):
                    continue

                return team_no

        def add_team_data(team_no, round_no, game_no, opponent_no):
            teams_data[team_no]['rounds'].append(round_no)
            teams_data[team_no]['games'].append(game_no)
            teams_data[team_no]['opponents'].append(team2)

        team1 = get_team()
        team2 = get_team(exclude_teams=[team1] + teams_data[team1]['opponents'])

        add_team_data(team1, round_no, game_no, team2)
        add_team_data(team2, round_no, game_no, team1)

        print("  game {}:  {} - {}".format(game_no, team1, team2))

print('')
