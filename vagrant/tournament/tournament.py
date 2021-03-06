#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM matches;")
    conn.commit()
    conn.close()
    """Remove all the match records from the database."""


def deletePlayers():
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM players;")
    conn.commit()
    conn.close()
    """Remove all the player records from the database."""


def countPlayers():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM players;")
    result = c.fetchall()
    conn.commit()
    conn.close()
#   print result[0][0]
    return result[0][0]
    """Returns the number of players currently registered."""


def registerPlayer(name):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO players(name) VALUES(%s);", (name,))
#    c.execute("SELECT COUNT(*) FROM players;")
#    count = c.fetchall()
#    print count[0][0]
    conn.commit()
    conn.close()
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """


def playerStandings():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM player_standings;")
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO matches(winner, loser) VALUES(%s, %s);", (winner, loser))
    conn.commit()
    conn.close()
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM player_standings;")
    result = c.fetchall()
    conn.commit()
    conn.close()
    output = []
    for e in range(len(result)):
        if e % 2 == 0:
            output.append(result[e][:2])
        else:
            match_number = e/2
            output[match_number] = output[match_number] + result[e][:2]
    print output
    return output
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


