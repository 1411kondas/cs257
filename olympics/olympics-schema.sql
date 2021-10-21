olympics=# CREATE TABLE athlete (
id integer,
full_name text);
CREATE TABLE

olympics=# CREATE TABLE athlete_data (
id integer,
sex text,
age integer,
height integer,
weight integer,
team text);
CREATE TABLE

olympics=# CREATE TABLE team_NOC (
NOC_id integer, 
NOC text,
team text);
CREATE TABLE

olympics=# CREATE TABLE game (
games text,
year integer,
season text,
city text);
CREATE TABLE

olympics=# CREATE TABLE athlete_event (
id integer,
games text,
sport text,
event text,
medal text);
CREATE TABLE

olympics=# CREATE TABLE medal (
NOC text,
gold int,
silver int,
bronze int);
CREATE TABLE
