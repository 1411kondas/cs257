'''
Sriya Konda
convert.py
Jeff Ondich
Adapted from code written by Jeff Ondich
'''

import csv

# Strategy:
# (1) Create a dictionary that maps athlete IDs to athlete names
#       and then save the results in athletes.csv
# (2) Create a dictionary that maps event names to event IDs
#       and then save the results in events.csv
# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
#
# NOTE: I'm doing these three things in three different passes through
# the athlete_events.csv files. This is not necessary--you can do it all
# in a single pass.


# (1) Create a dictionary that maps athlete_id -> athlete_name
#       and then save the results in athletes.csv
athletes = {}
original_data_file = open('/Users/sriyakonda/Desktop/athlete_events.csv', 'r')
reader = csv.reader(original_data_file)
athletes_file = open('/Users/sriyakonda/Desktop/athletes.csv', 'w')
writer = csv.writer(athletes_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    athlete_id = row[0]
    athlete_name = row[1]
    if athlete_id not in athletes:
        athletes[athlete_id] = athlete_name
        writer.writerow([athlete_id, athlete_name])
original_data_file.close()
athletes_file.close()

# (2) Create a dictionary that maps event_name -> event_id
#       and then save the results in events.csv
events = {}
original_data_file = open('/Users/sriyakonda/Desktop/athlete_events.csv', 'r')
reader = csv.reader(original_data_file)
events_file = open('/Users/sriyakonda/Desktop/events.csv', 'w')
writer = csv.writer(events_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    event_name = row[13]
    if event_name not in events:
        event_id = len(events) + 1
        events[event_name] = event_id
        writer.writerow([event_id, event_name])
original_data_file.close()
events_file.close()


# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
original_data_file = open('/Users/sriyakonda/Desktop/athlete_events.csv', 'r')
reader = csv.reader(original_data_file)
event_results_file = open('/Users/sriyakonda/Desktop/event_results.csv', 'w')
writer = csv.writer(event_results_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    athlete_id = row[0]
    event_name = row[13]
    event_id = events[event_name] # this is guaranteed to work by section (2)
    medal = row[14]
    writer.writerow([athlete_id, event_id, medal])
original_data_file.close()
event_results_file.close()


#Creates a csv file with all assocaited athlete data
    #For each row in original athlete_events.csv file,
    #build a row of new athlete_data.csv
original_data_file = open('/Users/sriyakonda/Desktop/athlete_events.csv', 'r')
reader = csv.reader(original_data_file)
athlete_data_file = open('/Users/sriyakonda/Desktop/athlete_data.csv', 'w')
writer = csv.writer(athlete_data_file)
heading_row = next(reader)
for row in reader:
    athlete_id = row[0]
    athlete_sex = row[2]
    athlete_age = row[3]
    athlete_height = row[4]
    athlete_weight = row[5]
    if athlete_age == "NA":
        athlete_age = 'NULL'
    #else:
    #    athlete_age = row[3]
    if athlete_height == "NA":
        athlete_height = 'NULL'
    #else:
    #    athlete_height = row[4]
    if athlete_weight == "NA":
        athlete_weight = 'NULL'
    #else:
    #    athlete_weight = row[5]
    athlete_team = row[6]
    writer.writerow([athlete_id, athlete_sex, athlete_age, athlete_height, athlete_weight, athlete_team])
original_data_file.close()
athlete_data_file.close()


#Creates a dictionary that maps NOC -> NOC_id and then saves the results in events.csv
#Creates a csv file with NOCs, NOC id numbers and countries
    #For each row in original athlete_events.csv file,
    #build a row of new team_NOC.csv
NOCs = {}
list_all_NOCs = []
second_data_file = open('/Users/sriyakonda/Desktop/noc_regions.csv', 'r')
reader = csv.reader(second_data_file)
team_NOC_file = open('/Users/sriyakonda/Desktop/team_NOC.csv', 'w')
writer = csv.writer(team_NOC_file)
heading_row = next(reader)
for row in reader:
    NOC_name = row[0]
    list_all_NOCs.append(NOC_name)
    team = row[1]
    if NOC_name not in NOCs: #Creates id numbers for each NOC
        NOC_id = len(NOCs) + 1
        NOCs[NOC_name] = NOC_id
        writer.writerow([NOC_id, NOC_name, team ])
second_data_file.close()
team_NOC_file.close()




#Creates three dictionaries, each to calculate the number of gold, silver and bronze metals won per NOC
#Creates a csv file with NOCs and the number of each metal types thay have won
    #For each row in original athlete_events.csv file,
    #build a row of new medal.csv
#temp = ["USA", "CHN", "FIN", "NOR", "NED", "EST", "DEN", "ROU", "FRA"]
gold_metals = {}
silver_metals = {}
bronze_metals = {}
#original_data_file = open('test.csv', 'r')
original_data_file = open('/Users/sriyakonda/Desktop/athlete_events.csv', 'r')
reader = csv.reader(original_data_file)
medal_file = open('/Users/sriyakonda/Desktop/medal.csv', 'w')
writer = csv.writer(medal_file)
heading_row = next(reader)
for row in reader:
    NOC_name = row[7]
    NOC_id = NOCs[NOC_name]
    if NOC_id not in gold_metals:
        gold_metals[NOC_id] = 0
    if "Gold" == row[14]:
        gold_metals[NOC_id] += 1
    if NOC_id not in silver_metals:
        silver_metals[NOC_id] = 0
    if "Silver" == row[14]:
        silver_metals[NOC_id] += 1
    if NOC_id not in bronze_metals:
        bronze_metals[NOC_id] = 0
    if "Bronze" == row[14]:
        bronze_metals[NOC_id] += 1
for country in NOCs:
    id = NOCs[country]
    writer.writerow([country, gold_metals[id], silver_metals[id], bronze_metals[id]])
original_data_file.close()
medal_file.close()



#Creates a csv file with all the athlete ids and all realted details to their sport/game/event
    #For each row in original athlete_events.csv file,
    #build a row of new athlete_game.csv
original_data_file = open('/Users/sriyakonda/Desktop/athlete_events.csv', 'r')
reader = csv.reader(original_data_file)
athlete_game_file = open('/Users/sriyakonda/Desktop/athlete_game.csv', 'w')
writer = csv.writer(athlete_game_file)
heading_row = next(reader)
for row in reader:
    athlete_id = row[0]
    athlete_games = row[8]
    athlete_year = row[9]
    athlete_sport = row[12]
    athlete_event = row[13]
    athlete_medal = row[14]
    if athlete_games == "NA":
        athlete_games = 'NULL'
    if athlete_year == "NA":
        athlete_year = 'NULL'
    if athlete_sport == "NA":
        athlete_sport = 'NULL'
    if athlete_event == "NA":
        athlete_event = 'NULL'
    if athlete_medal == "NA":
        athlete_medal = 'NULL'
    writer.writerow([athlete_id, athlete_games, athlete_year, athlete_sport, athlete_event, athlete_medal])
original_data_file.close()
athlete_game_file.close()


#Creates a csv file with basic information about all olymic games
    #For each row in original athlete_events.csv file,
    #build a row of new games.csv
game_all = {}
original_data_file = open('/Users/sriyakonda/Desktop/athlete_events.csv', 'r')
reader = csv.reader(original_data_file)
games_file = open('/Users/sriyakonda/Desktop/cs257/games.csv', 'w')
writer = csv.writer(games_file)
heading_row = next(reader)
for row in reader:
    game = row[8]
    year = row[9]
    season = row[10]
    city = row[11]
    if game not in game_all:
        game_id = len(game_all) + 1
        game_all[game] = game_id
        writer.writerow([game_id, game, year, season, city])
original_data_file.close()
games_file.close()
