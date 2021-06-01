
 

1. sql_queries.py :  We should read raw data first, then we have a business logical idea to design data modeling. 
    (A) Avoid error:  If there is a  duplicate key,  the Do nothing -> ON CONFLICT (song_id) DO NOTHING;
    
2. etl.py :  
    (A) songplays table :  "songplay_id" column is SERIAL PRIMARY KEY. It is auto increment primary key.  
    So I removed "index" columns in  line 63 , we don't need to specify the value for "songplay_id" column there.
    (B) There are a couple of columns on the artists table were not macth table columns in sql_queries.py, it cuase error shows up, I change columns name on sql_queries.py.
    
    
    
3. How do I run python: 
    (A) Console : !python etl.py -->Run 
    (B) _.ipynb : Run by line or block
    
4.  if there is another connection on database, How do i deal it ?
    (A) run coon.close()
    (b) restart kernel 
    (c) shout down all kernels
