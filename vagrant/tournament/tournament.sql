-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- DROP TABLE IF EXISTS dbo.Product
-- (SELECT count(*) as num FROM players, matches WHERE matches.player1 = players.id or matches.player2 = players.id) as matches_played

DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS matches;
CREATE DATABASE tournament;
\c tournament;
CREATE TABLE players(name text, id serial primary key);
CREATE TABLE matches(match_id serial primary key, winner int references players(id), loser int references players(id));

CREATE VIEW matches_names AS
	SELECT matches.match_id, a.name as winner, b.name as loser
	FROM matches, players as a, players as b
	WHERE a.id = matches.winner AND b.id = matches.loser;

CREATE VIEW games_won AS
	SELECT players.id as id, COALESCE(COUNT(matches.winner), 0) as wins 
	FROM players LEFT JOIN matches
	ON players.id = matches.winner
	GROUP BY id
	ORDER BY wins desc, id;