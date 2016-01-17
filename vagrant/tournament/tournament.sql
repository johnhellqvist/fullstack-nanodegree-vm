-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- DROP TABLE IF EXISTS dbo.Product

DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS matches;
CREATE DATABASE tournament;
\c tournament;
CREATE TABLE players(name text, id serial primary key);
CREATE TABLE matches(id serial primary key, winner int references players(id), loser int references players(id));

