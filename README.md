
# Files I updated:

1. sql_queries.py :  We should read raw data first, then we have a business logical idea to design data modeling. 
    * How to avoid error: 
     * If there is a  duplicate key,  the Do nothing -> ON CONFLICT (song_id) DO NOTHING;
     * If user_id is duplicate, example  updlate   the level of the user to paid  --> ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
         
    
    
12. etl.py :  
    * songplays table :  "songplay_id" column is SERIAL PRIMARY KEY. It is auto increment primary key. I removed "index" columns in  line 63. we don't need to specify the value for "songplay_id" column there.
    * There are a couple of columns on the artists table were not macth table columns in sql_queries.py. it cuase error shows up. I change columns name on sql_queries.py.
    
# Basic thing to know 

    
1. How do I run python: 
    * Console : !python etl.py -->Run 
    * __.ipynb : Run by line or block
    
2.  If there is another connection on database, How do i deal it ?
    *  run coon.close()
    * restart kernel 
    * shout down all kernels

3. How do I write comments in Python
    * clocstring : we can make mutile comments between two  the triple quotation marks   ''' xxxxxxxx '''
    * In-line comments: we use the hash symbol # to write a single-line comment.    #xxxxx

# Files in repository:
1. data folder: The metadata files written in JSON format.
2. create_tables.py: we can run this file to create table. It is realted to sql_queries.py
3. sql_queries: It is included SQL scripts which contains data schedume. 
4. etl.py: Import data into tables. 
5. etl.ipynb: Import data into tables. You can run by lines or blocks.
