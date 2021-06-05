# DROP TABLES

songplay_table_drop = " drop table if exists songplay ;"
user_table_drop = " drop table if exists users;"
song_table_drop = " drop table if exists songs ;"
artist_table_drop = " drop table if exists artists ;"
time_table_drop = " drop table if exists  time ;"

# CREATE TABLES

songplay_table_create = (""" create table songplays  ( 
    songplay_id  SERIAL PRIMARY KEY,
    start_time  timestamp NOT NULL FOREIGN KEY REFERENCES time(start_time),
    user_id varchar(255) FOREIGN KEY REFERENCES users(user_id),
    level  varchar(10),
    song_id VARCHAR(255) FOREIGN KEY REFERENCES songs(song_id),
    artist_id VARCHAR(255) FOREIGN KEY REFERENCES artists(artist_id),
    session_id int, 
    location varchar(255),
    user_agent varchar(255) 
    );
""")

user_table_create = (""" create table users ( 
    user_id varchar(255) PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    gender char(1) ,
    level varchar(10)
    );
""")

song_table_create = (""" create table songs ( 
    song_id VARCHAR(255) PRIMARY KEY,
    title  VARCHAR(255),
    artist_id VARCHAR(255),
    year int ,
    duration NUMERIC (10, 5) 
    );
""")

artist_table_create =( """
CREATE TABLE IF NOT EXISTS artists 
    (
        artist_id varchar NOT NULL PRIMARY KEY, 
        artist_name varchar, 
        artist_location varchar,
        artist_latitude NUMERIC (10, 5) ,
        artist_longitude NUMERIC (10, 5) 
    );
""") 

time_table_create = (""" create table time (
    start_time timestamp PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int,
    weekday int
); 
""")

# INSERT RECORDS

songplay_table_insert = (""" insert into songplays 
( songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent ) 
 VALUES(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (songplay_id) DO NOTHING; 
""")

user_table_insert = (""" insert into users 
( user_id, first_name, last_name, gender, level ) values 
( %s, %s,%s,%s,%s )
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id, title, artist_id, year, duration
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")


artist_table_insert = (""" insert into artists
( artist_id,  artist_name ,  artist_location,  artist_latitude,  artist_longitude ) VALUES 
( %s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = (""" insert into time 
( start_time, hour, day, week, month, year, weekday ) 
VALUES ( %s, %s, %s, %s,%s,%s, %s )
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT song_id, songs.artist_id
FROM songs JOIN artists ON songs.artist_id=artists.artist_id
WHERE title=%s AND artists.artist_name=%s AND duration=%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]