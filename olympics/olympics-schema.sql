olympics=# CREATE TABLE athlete (
id integer,
full_name text);
CREATE TABLE

olympics=# CREATE TABLE athlete_data (
id integer,
sex text,
age integer,
height float,
weight float,
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

olympics=# CREATE TABLE athlete_game (
id integer,
games text,
year integer,  
sport text,
event text,
medal text);
CREATE TABLE

olympics=# CREATE TABLE medal (
NOC text,
gold integer,
silver integer,
bronze integer);
CREATE TABLE
