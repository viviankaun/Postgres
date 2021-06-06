
# Files I updated:

1. sql_queries.py :  We should read raw data first, then we have a business logical idea to design data modeling. 
    (A). How to avoid error: 
         * If there is a  duplicate key,  the Do nothing -> ON CONFLICT (song_id) DO NOTHING;
         * If user_id is duplicate, example  updlate   the level of the user to paid  --> ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
         
    
    
12. etl.py :  
    * songplays table :  "songplay_id" column is SERIAL PRIMARY KEY. It is auto increment primary key. I removed "index" columns in  line 63 , we don't need to specify the value for "songplay_id" column there.
    * There are a couple of columns on the artists table were not macth table columns in sql_queries.py, it cuase error shows up, I change columns name on sql_queries.py.
    
# Import thing to know from this session 

    
>. How do I run python: 
    (A) Console : !python etl.py -->Run 
    (B) _.ipynb : Run by line or block
    
.  If there is another connection on database, How do i deal it ?
    (A) run coon.close()
    (b) restart kernel 
    (c) shout down all kernels

5. (A) clocstring : we can make mutile command  between two  the triple quotation marks   ''' xxxxxxxx '''
   (B) In-line comments:
