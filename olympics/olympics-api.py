'''
    olympics-api.py
    Sriya Konda, 28 October 2021
    Jeff Ondich, CS257
    Updated 7 October 2020
'''

import sys
import argparse
import flask
import json
import psycopg2

password = 'sriya1411'
user = 'sriyakonda'
database = 'olympics'


app = flask.Flask(__name__)

try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print(e)
    exit()

@app.route('/help')
def get_help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)



@app.route('/games')
def games():
    games_list = []
    try:
        cursor = connection.cursor()
        query = '''SELECT game.games, game.games_id, game.year, game.season, game.city
                   FROM game
                   ORDER BY game.year'''
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    print('===== Games and its details =====')
    for row in cursor:
        temp_dic = {row[0]: {"Game ID": row[1], "Game Year": row[2], "Season": row[3], "City": row[4]}}
        games_list.update(temp_dic)
    return json.dumps(games_list)



@app.route('/nocs')
def get_nocs():
    NOC_team_list = []
    try:
        cursor = connection.cursor()
        query = SELECT team_NOC.NOC
                   FROM team_NOC
                   WHERE team_NOC.NOC IS NOT NULL
                   ORDER BY team_NOC.NOC ASC;
        cursor.execute(query)
        except Exception as e:
        print(e)
        exit()
    print('===== NOC and Teams =====')
    for row in cursor:
        temp_dic = {"NOC": row[0], "Team": row[1]}
        NOC_team_list.append(temp_dic)
    return json.dumps(NOC_team_list)



@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')
def get_medalists():
    medal_lists = []
    games_id = flask.request.args.get('games_id', type=int)
    noc = flask.request.args.get('noc_abbreviation')
    try:
        cursor = connection.cursor()
        query = SELECT athlete.id, athlete.full_name, athlete_data.sex, athlete_game.sport, athlete_game.event, athlete_game.medal
                   FROM athlete, athlete_data, athlete_game, game
                   WHERE athlete_game.medal IS NOT NULL
                   AND team_NOC = %s 
                   AND athlete_data.team = team_NOC.team
                   AND games.games_id = %s
                   AND athlete_game.games = game.games
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    print('===== Medalists Data =====')
    for row in cursor:
        temp_dic = {"ID": row[0], "Name": row[1], "Sex" : row[2], "Sport" : row[3], "Event" : row[4], "Medal" : row[5], }
        medal_lists.append(temp_dic)
    return json.dumps(medal_lists)


'''