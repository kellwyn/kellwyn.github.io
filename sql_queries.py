# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""create table songplays 
(songplay_id SERIAL PRIMARY KEY,
start_time timestamp REFERENCES time(start_time),
user_id int REFERENCES users(user_id),
level text,
song_id text REFERENCES songs(song_id),
artist_id text REFERENCES artists(artist_id),
session_id int,
location varchar(256), 
user_agent varchar(256));
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users
(user_id int, first_name text, last_name text, gender text, level text
);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs
(song_id text, title text, artist_id text, year int, duration float
);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
(artist_id text, artist_name text, artist_location text, artist_latitude float, artist_longitude float
);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time
(start_time Timestamp, hour int, day int, week int, month int, year int, weekday text
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title=%s  AND artists.artist_name=%s AND songs.duration=%s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]