# MODULE IMPORT
import sys, os, json
sys.path.append('/Users/kimdohoon/git/football-data-pipeline/lib')
import football_lib as lib

# READ LEAGUE ID
params_before = lib.read_Params("api_league_id", "pipe_league")

uri_list = []
for values in params_before:
    # READ TEAM ID
    params = lib.read_Params("*", "pipe_team", {"api_league_id" : values[0]})

    # MAKE URI
    for count in range(len(params)):
        for page in range(5):
            league_id = params[count][3]
            team_id = params[count][2]

            params_dict = {"league" : league_id,
                           "team" : team_id,
                           "season" : "2023",
                           "page" : page}
            uri = lib.make_uri("players", params_dict)
            uri_list.append(uri)

# TEST
print(uri_list[:5])