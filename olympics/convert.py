'''
    Sriya Konda
    convert.py
    Jeff Ondich, 14 October 2021
'''

import csv
import athlete_events.csv.zip
import noc_region.csv


#file = pd.read_csv("athlete_events.csv.zip")
#file2= pd.read_csv("noc_region.csv")


file = open('athlete_events.csv.zip')
reader = csv.reader(file)
for row in reader:
    id_number = row[0]
    full_name = row[1]
    sex = row[2]
    age = int(row[3])
    height = int(row[4])
    weight = int(row[5])
    team = row[6]
    NOC = row[7]
    games = row[8]
    year = int(row[9])
    season = row[10]
    city = row[11]
    sport = row[12]
    sport = row[13]
    medal = row[14]

    #names_seperates = full_name.split(' ')
    #    firstName = names_seperates[0]
    #    lastName = names_seperates[0]

file = open('noc_region.csv')
reader = csv.reader(file)
for row in reader:
    NOC = row[0]
    region = row[1]
    notes = row[2]


athlete.csv = open('athlete_events.csv.zip', 'w')
writer = csv.writer(athlete.csv)
writer.writerow(id_number)
writer.writerow(full_name)
athlete.csv.close()

athlete_biodata.csv = open('athlete_events.csv.zip', 'w')
writer = csv.writer(athlete_biodata.csv)
writer.writerow(id_number)
writer.writerow(sex)
writer.writerow(age)
writer.writerow(height)
writer.writerow(weight)
athlete_biodata.csv.close()

athlete_team.csv = open('athlete_events.csv.zip', 'w')
writer = csv.writer(athlete_team.csv)
writer.writerow(id_number)
writer.writerow(team)
writer.writerow(NOC)
athlete_team.csv.close()

region_NOC.csv = open('noc_region.csv.zip', 'w')
writer = csv.writer(region_NOC.csv)
writer.writerow(NOC)
writer.writerow(region)
region_NOC.csv.close()

game.csv = open('athlete_events.csv.zip', 'w')
writer = csv.writer(game.csv)
writer.writerow(games)
writer.writerow(year)
writer.writerow(season)
writer.writerow(city)
game.csv.close()

athlete_event.csv = open('athlete_events.csv.zip', 'w')
writer = csv.writer(athlete_event.csv)
writer.writerow(id_number)
writer.writerow(games)
writer.writerow(sport)
writer.writerow(event)
writer.writerow(medal)
athlete_event.csv.close()
