#List all the medals won by Greg Louganis, sorted by year.
#Include whatever fields in this output that you think appropriate.

SELECT athlete_event.games, athlete_event.sport, athlete_event.event, athlete_event.medal
FROM athlete_event,  athlete
WHERE athlete.id = athlete_event.id
AND athlete_event.medal IS NOT NULL
AND athlete.full_name = 'Greg Louganis'
ORDER BY athlete_event.year;





#List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation.
#These entities, by the way, are mostly equivalent to countries. But in some cases,
#you might find that a portion of a country
#participated in a particular games (e.g. one guy from Newfoundland in 1904) or some other oddball situation

SELECT region_NOC.NOC
FROM region_NOC
WHERE region_NOC.NOC IS NOT NULL
ORDER BY region_NOC.NOC ASC;





#List the names of all the athletes from Kenya.
#If your database design allows it, sort the athletes by last name.

SELECT athlete_data.team, athlete.full_name
FROM athlete_data, athlete
WHERE athlete_data.team = 'Kenya';





#List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.

SELECT medal.NOC, medal.gold
FROM medal.gold, medal.NOC
WHERE medal.gold IS NOT NULL
ORDER BY medal.gold DESC;
