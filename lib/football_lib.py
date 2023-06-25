import mysql.connector as mc
import requests, json

def MySQL_Connection():
    global conn
    conn = mc.connect(user='root', \
                      password= 'tmzkdnxj1', \
	                    host='34.64.214.96', \
	                    database = 'scout', \
	                    port = '3306')
    print("Hi! SQL")

def read_Params(keyword, table, external: dict = None):
    MySQL_Connection()
    global conn
    cursor = conn.cursor()
    QUERY = f"SELECT {keyword} FROM {table} "
    if external != None:
        QUERY += "WHERE "
        QUERY += " AND ".join([f"{key}={value}" for key, value in external.items()])
        QUERY = QUERY.rstrip("AND")
    # TEST
    print(QUERY)
    cursor.execute(QUERY)
    fetched = cursor.fetchall()
    return fetched

def make_uri(keyword, params: dict):
    base = f"https://v3.football.api-sports.io/{keyword}?"
    for key, value in params.items():
        base += key + "=" + str(value) + "&"
        uri = base.rstrip("&")
    return uri

def make_json(uri_list, DIRECTORY, api_keys):
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': api_keys
    }
    for values in uri_list:
        uri = values["uri"]
        filename = values["filename"]
        # GET RESPONSE
        response = requests.request("GET", uri, headers=headers).json()
        # FILE WRITE
        with open(f"{DIRECTORY}/{filename}", "w") as file:
            json.dump(response, file, indent=4)
            print(filename + " load is done")

# TEST - players with 1 team id
if __name__ == "__main__":
    params = read_Params("api_league_id", "pipe_league")
    params_2 = read_Params("*", "pipe_team", {"api_league_id": params[0][0]})
    for cnt in range(5):
        test_dict = {"league": params_2[0][3], "team": params_2[0][2], "season": "2023", "page": cnt}
        print(test_dict)
        uri = make_uri("players", test_dict)
        print(uri)