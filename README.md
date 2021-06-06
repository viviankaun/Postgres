
# Files I updated:

1. sql_queries.py :  We should read raw data first, then we have a business logical idea to design data modeling. 
    (A). How to avoid error: 
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

3. * clocstring : we can make mutile command  between two  the triple quotation marks   ''' xxxxxxxx '''
   * In-line comments:
