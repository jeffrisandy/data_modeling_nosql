# CREATE TABLES
## session_history table
session_table_create = """CREATE TABLE IF NOT EXISTS session_history (
                            sessionID int, 
                            itemInSession int, 
                            artist text, 
                            song_title text, 
                            song_length float, 
                            PRIMARY KEY (sessionID, itemInSession)
                        )"""

## user_history table
user_table_create = """CREATE TABLE IF NOT EXISTS user_history (
                        userID int, 
                        sessionID int, 
                        itemInSession int, 
                        artist text, 
                        song_title text, 
                        first_name text, 
                        last_name text, 
                        PRIMARY KEY ((userID, sessionID), itemInSession)
                    )"""

## song_history table
song_table_create = """CREATE TABLE IF NOT EXISTS song_history (
                        song_title text, 
                        userID int, 
                        first_name text, 
                        last_name text,
                        PRIMARY KEY (song_title, userID)
                    )"""

## INSERT TABLE

session_table_insert = """INSERT INTO session_history (
                            sessionID, 
                            itemInSession, 
                            artist, 
                            song_title, 
                            song_length)
                            VALUES (%s, %s, %s, %s, %s)"""

user_table_insert = """INSERT INTO user_history (
                            userID, 
                            sessionId, 
                            itemInSession, 
                            artist, 
                            song_title, 
                            first_name, 
                            last_name)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)"""

song_table_insert = """INSERT INTO song_history (
                            song_title, 
                            userID, 
                            first_name, 
                            last_name)
                            VALUES (%s, %s, %s, %s)"""

# DROP TABLES
session_table_drop = "DROP TABLE IF EXISTS session_history"
user_table_drop = "DROP TABLE IF EXISTS user_history"
song_table_drop = "DROP TABLE IF EXISTS song_history"


# QUERY LISTS
create_table_queries = [session_table_create, user_table_create, song_table_create]
drop_table_queries = [session_table_drop, user_table_drop, song_table_drop]
