olympics=# CREATE TABLE athlete (
id SERIAL,
last_name text,
first_name text);
CREATE TABLE

olympics=# CREATE TABLE athlete_biodata (
id SERIAL,
sex text,
age integer,
height integer,
weight integer);
CREATE TABLE

olympics=# CREATE TABLE athlete_team (
id SERIAL,
team text,
NOC text);
CREATE TABLE

olympics=# CREATE TABLE region_NOC (
NOC text,
region text);
CREATE TABLE

olympics-# CREATE TABLE game (
games text,
year integer,
season text,
city text);
CREATE TABLE

olympics-# CREATE TABLE athlete_event (
id SERIAL,
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

olympics=# CREATE TABLE athlete_medal (
id SERIAL,
game text,
year integer,
sport text,
event text,
gold int,
silver int,
bronze int);
CREATE TABLE
