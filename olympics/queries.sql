#List all the medals won by Greg Louganis, sorted by year.
#Include whatever fields in this output that you think appropriate.

SELECT athlete_game.games, athlete_game.sport, athlete_game.event, athlete_game.medal
FROM athlete, athlete_game
WHERE athlete.id = athlete_game.id
AND athlete_game.medal IS NOT NULL
AND athlete.full_name = 'Greg Louganis'
ORDER BY athlete_game.year;



#List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation.
#These entities, by the way, are mostly equivalent to countries. But in some cases,
#you might find that a portion of a country
#participated in a particular games (e.g. one guy from Newfoundland in 1904) or some other oddball situation

SELECT team_NOC.NOC
FROM team_NOC
WHERE team_NOC.NOC IS NOT NULL
ORDER BY team_NOC.NOC ASC;



#List the names of all the athletes from Kenya.
#If your database design allows it, sort the athletes by last name.

SELECT athlete.full_name
FROM athlete_data, athlete
WHERE athlete.id = athlete_data.id 
AND athlete_data.team = 'Kenya';



#List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.

SELECT medal.NOC, medal.gold
FROM medal
WHERE medal.gold IS NOT NULL
ORDER BY medal.gold DESC;
